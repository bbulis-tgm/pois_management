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
    housenumber = ""
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

    def get_id(self):
        return self.id

    def set_category(self, category):
        self.category = category

    def get_category(self):
        return self.category

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_icon(self, icon):
        self.icon = icon

    def get_icon(self):
        return self.icon

    def set_lati(self, lati):
        self.lati = lati

    def get_lati(self):
        return self.lati

    def set_long(self, long):
        self.long = long

    def get_long(self):
        return self.long

    def set_countrycode(self, countrycode):
        self.countrycode = countrycode

    def get_countrycode(self):
        return self.countrycode

    def set_postalcode(self, postalcode):
        self.postalcode = postalcode

    def get_postalcode(self):
        return self.postalcode

    def set_city(self, city):
        self.city = city

    def get_city(self):
        return self.city

    def set_street(self, street):
        self.street = street

    def get_street(self):
        return self.street

    def set_housenumber(self, housenumber):
        self.housenumber = housenumber

    def get_housenumber(self):
        return self.housenumber

    def set_info(self, info):
        self.info = info

    def get_info(self):
        return self.info

    def set_phone(self, phone):
        self.phone = phone

    def get_phone(self):
        return self.phone

    def to_string(self):
        return "POI(" + self.id + ", " + self.category + ", " + self.name + ", (" + self.lati + ", " + self.long + "), " + self.countrycode + ", " + self.postalcode + ", " + self.city + ", " + self.street + ", " + self.housenumber + ", " + self.info + ", " + self.phone + ")"