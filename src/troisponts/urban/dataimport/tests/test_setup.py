# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from troisponts.urban.dataimport.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of troisponts.urban.dataimport into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if troisponts.urban.dataimport is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('troisponts.urban.dataimport'))

    def test_uninstall(self):
        """Test if troisponts.urban.dataimport is cleanly uninstalled."""
        self.installer.uninstallProducts(['troisponts.urban.dataimport'])
        self.assertFalse(self.installer.isProductInstalled('troisponts.urban.dataimport'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that ITroispontsUrbanDataimportLayer is registered."""
        from troisponts.urban.dataimport.interfaces import ITroispontsUrbanDataimportLayer
        from plone.browserlayer import utils
        self.failUnless(ITroispontsUrbanDataimportLayer in utils.registered_layers())
