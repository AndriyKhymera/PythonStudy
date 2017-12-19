class Product(object):
    Product_Type = ""
    Vendor = ""
    Product = ""
    Version = ""
    Update = ""
    Edition = ""
    Language = ""

    def __init__(self, dictionary):
        if "Product_Type" in dictionary:
            self.Product_Type = dictionary["Product_Type"]
        if "Vendor" in dictionary:
            self.Vendor = dictionary["Vendor"]
        if "Product" in dictionary:
            self.Product = dictionary["Product"]
        if "Version" in dictionary:
            self.Version = dictionary["Version"]
        if "Update" in dictionary:
            self.Update = dictionary["Update"]
        if "Edition" in dictionary:
            self.Edition = dictionary["Edition"]
        if "Language" in dictionary:
            self.Language = dictionary["Language"]