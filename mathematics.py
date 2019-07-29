from docutils.nodes import Text
from docutils.parsers.rst import directives
from sphinx import addnodes
from sphinx.domains import ObjType
from sphinx.roles import XRefRole
from sphinx.util import ws_re
from sphinxcontrib.domaintools import CustomDomain, GenericObject


class MathematicsDomain(CustomDomain):
    name = 'm'
    label = 'Mathematics'

    @classmethod
    def add_directive(cls, name, directive):
        directive.domain = cls
        cls.object_types[name] = ObjType(name, name)
        cls.directives[name] = directive
        cls.roles[name] = XRefRole()

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


class Theorem(GenericObject):
    indextemplate = 'single:%s;'
    prefix = '定理'
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



def setup(app):
    MathematicsDomain.add_directive('theorem', Theorem)
    app.add_domain(MathematicsDomain)

