
from v_gd import Vgd

ISGD_SERVICE_URL = "http://is.gd/%s.php"

class Isgd(Vgd):
    def __init__(self):
        Vgd.__init__(self)
        self.service_url = ISGD_SERVICE_URL

