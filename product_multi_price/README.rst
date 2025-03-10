===================
Product Multi Price
===================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:db3e0600440dcafca889e339211f83be9973bd8907045d52490e64e8787e1645
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fproduct--attribute-lightgray.png?logo=github
    :target: https://github.com/OCA/product-attribute/tree/15.0/product_multi_price
    :alt: OCA/product-attribute
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/product-attribute-15-0/product-attribute-15-0-product_multi_price
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/product-attribute&target_branch=15.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

This module allows to set multiple prices to products and base pricelist
rules on them.

**Table of contents**

.. contents::
   :local:

Configuration
=============

To configure multiple prices you need to set multi prices field names first.
To do so, you need admin permissions. Then go to:

#. *Settings > Technical > Database Structure > Price Field Names*
#. Create the multi price fields you need.

If you have multiple companies, you can assign independent field sets for each
one.

Note: 'Show multi prices' access group must be checked to be able to
add multiple prices in the product form view.

Usage
=====

To use this module, you need to:

#. Go to the product page.
#. In the general tab, there's a list called *Other Prices*.
#. You can add one for every price name available.

To base pricelist rules on that fields, in the pricelist:

#. Add a rule and choose *formula* as the computing method.
#. In the *Based on* dropdown list, select *Other Price*.
#. A new list appear: *Other Price Name*. Pick the one you need.
#. Configure the formula.
#. Now the rule is based on that price for the products that have it
   configured. Otherwise, it will return 0.

Known issues / Roadmap
======================

* Add mechanisms that allow to set multiprices values from external flows. For
  example: having AVCO, FIFO and Standard prices computed simultaneously in
  this table.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/product-attribute/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/product-attribute/issues/new?body=module:%20product_multi_price%0Aversion:%2015.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Tecnativa

Contributors
~~~~~~~~~~~~

* `Tecnativa <https://www.tecnativa.com>`_

  * David Vidal
  * Pedro M. Baeza
  * Ernesto Tejeda

Maintainers
~~~~~~~~~~~

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the `OCA/product-attribute <https://github.com/OCA/product-attribute/tree/15.0/product_multi_price>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
