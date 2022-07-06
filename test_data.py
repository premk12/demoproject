import pytest

from Base_class import Base_class


@pytest.mark.usefixtures("loaddata")
class Testdata2(Base_class):
    def test_editprofile(self,loaddata):
        log=self.getLogger()
        log.debug(loaddata[0])
        print(loaddata[1])







