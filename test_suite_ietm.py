# import pytest
# from .steps.viewer_structure_erd import
# from .steps.search_engine import
# from .steps.viewer_descriptive_md import
# from .steps.viewer_procedural_md import
# from .steps.viewer_electronic_catalogs_lists_md import
# from .steps.viewer_troubleshooting_procedures_md import
# from .steps.viewer_consumption_rates_spare_parts_materials_md import
# from .steps.viewer_maintenance_regulations_md import
# from .steps.viewer_electrical_installation_md import
# from .steps.localization_failed_element import
# from .steps.viewer_instructions_crew_md import
# from .steps.diagnostics_failure import
# from .steps.viewer_process_md_selected_product_configuration import
# from .steps.display_identification_part_process_md import
# from .steps.viewer_process_md_interactive_scenario_ietm import

# class TestPMI():
#
#     @pytest.fixture(scope="function", autouse=True)
#     def setup(self, browser):
#         link = "http://localhost:8082/"
#         login_page = LoginPage(browser, link)
#         login_page.open()
#         login_page.go_to_login_page()
#         email = str(time.time()) + "@fakemail.org"
#         password = "128mb256kb512gb"
#         login_page.register_new_user(email, password)
#         login_page.should_be_authorized_user()
#
#     @pytest.mark.pmi
#     def test_TC85(self, browser):
#         link = "http://localhost:8082/"

    # @pytest.mark.pmi
    # def test_TC86(self, browser):
    #   link = "http://localhost:8082/"
    #
    #
    # @pytest.mark.pmi
    # def test_TC87(self, browser):
    #   link = "http://localhost:8082/"
    #
    #
    # @pytest.mark.pmi
    # def test_TC88(self, browser):
    #   link = "http://localhost:8082/"
    #
    #
    # @pytest.mark.pmi
    # def test_TC89(self, browser):
    #   link = "http://localhost:8082/"
    #
    #
    # @pytest.mark.pmi
    # def test_TC90(self, browser):
    #   link = "http://localhost:8082/"
    #
    #
    # @pytest.mark.pmi
    # def test_TC91(self, browser):
    #   link = "http://localhost:8082/"
    #
    #
    # @pytest.mark.pmi
    # def test_TC92(self, browser):
    #   link = "http://localhost:8082/"
    #
    #
    # @pytest.mark.pmi
    # def test_TC93(self, browser):
    #   link = "http://localhost:8082/"
    #
    #
    # @pytest.mark.pmi
    # def test_TC95(self, browser):
    #   link = "http://localhost:8082/"
    #
    #
    # @pytest.mark.pmi
    # def test_TC96(self, browser):
    #   link = "http://localhost:8082/"
    #
    #
    # @pytest.mark.pmi
    # def test_TC102(self, browser):
    #   link = "http://localhost:8082/"
    #
    #
    # @pytest.mark.pmi
    # def test_TC103(self, browser):
    #   link = "http://localhost:8082/"
    #
    #
    # @pytest.mark.pmi
    # def test_TC104(self, browser):
    #   link = "http://localhost:8082/"
    #
    #
    # @pytest.mark.pmi
    # def test_TC105(self, browser):
    #   link = "http://localhost:8082/"