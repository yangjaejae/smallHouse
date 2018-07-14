from django.contrib import admin

from smallHouse.models import SmallHouseRealestate
from smallHouse.models import SmallHouseRealnews

from smallHouse.models import RealestateIconPath
from smallHouse.models import TransIconPath

from smallHouse.models import LocationCode

from smallHouse.models import SchoolInfo
from smallHouse.models import CrimeInfo
from smallHouse.models import TransInfo

admin.site.register(SmallHouseRealestate)
admin.site.register(SmallHouseRealnews)

admin.site.register(RealestateIconPath)
admin.site.register(TransIconPath)

admin.site.register(LocationCode)

admin.site.register(SchoolInfo)
admin.site.register(CrimeInfo)
admin.site.register(TransInfo)
