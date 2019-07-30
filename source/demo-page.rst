線形写像
=========

.. toctree::
   :caption: Contents:
   :maxdepth: 2

線形写像
+++++++++++++++++++++

.. m:def:: 線形写像

   | :math:`f:\mathbb{R}^{n}\rightarrow \mathbb{R}^{m}` :線形写像
   |    :math:`\overset{\mathrm{def}}{\Leftrightarrow}\mathbb{R}^n` の任意のベクトル :math:`\boldsymbol{v}, \boldsymbol{w}` および任意の実数 :math:`\lambda, \mu` に対し，

   .. math:: (\lambda \boldsymbol{v}+\mu \boldsymbol{w}) = \lambda f(\boldsymbol{v}) + \mu f(\boldsymbol{w})

.. m:prop:: 線形写像の合成

   | :math:`f:\mathbb{R}^{n}\rightarrow \mathbb{R}^{m},\ g:\mathbb{R}^{m}\rightarrow \mathbb{R}^{l}` : 線形
   |  :math:`\Rightarrow g\circ f: \mathbb{R}^{n}\rightarrow \mathbb{R}^{l}` : 線形

   .. m:pf::

      | :math:`\mathbb{R}^n` の任意のベクトル :math:`\boldsymbol{v}, \boldsymbol{w}` および任意の実数 :math:`\lambda, \mu` に対し， :m:def:`線形写像` より，

      .. math::

         g \circ f(\lambda\boldsymbol{v} + \mu\boldsymbol{w}) &= g \left( f(\lambda\boldsymbol{v} + \mu\boldsymbol{w}) \right)\\
            &= g \left( \lambda f(\boldsymbol{v}) + \mu f(\boldsymbol{w}) \right) \\
            &= \lambda g \circ f(\boldsymbol{v}) + \mu g \circ f(\boldsymbol{w}) \\
