import time
import pytest
from test_lib.rtt_data import config
from test_lib.api import ValidationApi
from test_lib.constants import TelltaleStatus, Buttons
class TestAbs(ValidationApi):

    @pytest.fixture
    def before(self):
        self.setup_logger()
        self.get_url("file:///D:/Automation_testing/webpage/cluster_hmi.html")
        self.icon_db_load()
        self.abs_icon = config["rtt"]["abs_icon"]
        self.abs_yellow_icon = config["rtt"]["abs_yellow_icon"]
        self.tpms_icon = config["rtt"]["tpms_icon"]
        yield
        self.press_btn(Buttons.Home.value)
    
    def test_tpms_on(self, before):
        """
        This test method will verify whether the tire presure icon is ON in the cluster HMI screen
        when tire pressure button is pressed.
        """
        self.press_btn(Buttons.TIRE_PRESSURE.value)
        time.sleep(7)
        
        frame  = self.capture_screen()
        self.verify_telltale_status(TelltaleStatus.ON.value, icon_data= self.tpms_icon, frame_data=frame)