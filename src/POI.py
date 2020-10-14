class POI:
    id = 0
    category = ""
    name = ""
    icon = ""
    lati = 0.0
    long = 0.0
    countrycode = ""
    postalcode = 0
    city = ""
    street = ""
    housenumber = 0
    info = ""
    phone = ""

    def __init__(self, id, category, name, icon, lati, long, countrycode, postalcode, city, street, housenumber, info, phone):
        self.id = id
        self.category = category
        self.name = name
        self.icon = icon
        self.lati = lati
        self.long = long
        self.countrycode = countrycode
        self.postalcode = postalcode
        self.city = city
        self.street = street
        self.housenumber = housenumber
        self.info = info
        self.phone = phone

    def set_id(self, id):
        self.id = id

    def get_id(self) -> int:
        return self.id

    def set_category(self, category):
        self.category = category

    def get_category(self) -> str:
        return self.category

    def set_name(self, name):
        self.name = name

    def get_name(self) -> str:
        return self.name

    def set_icon(self, icon):
        self.icon = icon

    def get_icon(self) -> str:
        return self.icon

    def set_lati(self, lati):
        self.lati = lati

    def get_lati(self) -> float:
        return self.lati

    def set_long(self, long):
        self.long = long

    def get_long(self) -> float:
        return self.long

    def set_countrycode(self, countrycode):
        self.countrycode = countrycode

    def get_countrycode(self) -> int:
        return self.countrycode

    def set_postalcode(self, postalcode):
        self.postalcode = postalcode

    def get_postalcode(self) -> int:
        return self.postalcode

    def set_city(self, city):
        self.city = city

    def get_city(self) -> str:
        return self.city

    def set_street(self, street):
        self.street = street

    def get_street(self) -> str:
        return self.street

    def set_housenumber(self, housenumber):
        self.housenumber = housenumber

    def get_housenumber(self) -> int:
        return self.housenumber

    def set_info(self, info):
        self.info = info

    def get_info(self) -> str:
        return self.info

    def set_phone(self, phone):
        self.phone = phone

    def get_phone(self) -> str:
        return self.phone