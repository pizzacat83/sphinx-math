from docutils.nodes import Admonition, Element, Text
from docutils.parsers.rst import directives
from sphinx import addnodes
from sphinx.domains import ObjType
from sphinx.locale import admonitionlabels
from sphinx.roles import XRefRole
from sphinx.util import ws_re
from sphinxcontrib.domaintools import CustomDomain, GenericObject


class MathematicsDomain(CustomDomain):
    name = 'm'
    label = 'Mathematics'

    @classmethod
    def add_directive(cls, name, directive):
        directive.domain = cls
        cls.directives[name] = directive

    @classmethod
    def add_object(cls, name, directive):
        cls.object_types[name] = ObjType(name, name)
        cls.roles[name] = XRefRole()
        cls.add_directive(name, directive)

    def resolve_xref(self, env, fromdocname, builder,
                     typ, target, node, contnode):
        if target == contnode.children[0].astext():
            contnode.children = (
                [Text('{} {} ({})'.format(
                    self.directives[typ].prefix,
                    '1.1.1',  # TODO: use correct number
                    target
                ))]
            )
        return super().resolve_xref(env, fromdocname, builder,
                                    typ, ws_re.sub('', target), node, contnode)



    '''


class MathematicsObject(GenericObject):
    indextemplate = 'single:%s;'
    prefix = ''
    object_spec = {
        'noindex': directives.flag,
        'anonymous': directives.flag,
    }

    def parse_node(self, env, sig, signode):
        signode += addnodes.desc_name(self.prefix, self.prefix)
        signode += addnodes.desc_type(' ', ' ')

        signode += addnodes.desc_type(*['({})'.format(sig)]*2)  # 第2引数が見た目になる
        name = ws_re.sub('', sig)
        return name


class Theorem(MathematicsObject):
    prefix = '定理'


class Definition(MathematicsObject):
    prefix = '定義'


class Proposition(MathematicsObject):
    prefix = '命題'


class MathematicsAdmonition(Admonition, Element):
    label = ''
    name = ''

    @classmethod
    def register(cls, app):
        admonitionlabels[cls.name] = cls.label

        def visit_node(self, node):
            self.visit_admonition(node, cls.name)

        def depart_node(self, node):
            self.depart_admonition(node)

        # TODO: support latex, plaintext
        app.add_node(cls,
                     html=(visit_node, depart_node))


class ProofAdmonition(MathematicsAdmonition):
    label = '証明'
    name = 'proof'


class Proof(directives.admonitions.BaseAdmonition):
    node_class = ProofAdmonition


def visit_proof_node(self, node):
    self.visit_admonition(node, 'proof')


def depart_proof_node(self, node):
    self.depart_admonition(node)


def setup(app):
    MathematicsDomain.add_object('thm', Theorem)
    MathematicsDomain.add_object('def', Definition)
    MathematicsDomain.add_object('prop', Proposition)
    MathematicsDomain.add_directive('pf', Proof)
    ProofAdmonition.register(app)
    app.add_domain(MathematicsDomain)

