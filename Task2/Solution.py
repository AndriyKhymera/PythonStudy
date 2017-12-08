import requests
import sys
from lxml import html
from lxml import cssselect

# Constants
ERROR_CLASS_NAME = "errormsg"

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

class CVEDetails(object):
    CVSS_Score = 0
    Confidentiality_Impact = ""
    Integrity_Impact = ""
    Availability_Impact = ""
    Access_Complexity = ""
    Authentication = ""
    Gained_Access = ""
    Vulnerability_type = ""
    CWE_ID = ""

    def __init__(self, dictionary):
        if "CVSS_Score" in dictionary:
            self.CVSS_Score = dictionary["CVSS_Score"]
        if "Confidentiality_Impact" in dictionary:
            self.Confidentiality_Impact = dictionary["Confidentiality_Impact"]
        if "Integrity_Impact" in dictionary:
            self.Integrity_Impact = dictionary["Integrity_Impact"]
        if "Availability_Impact" in dictionary:
            self.Availability_Impact = dictionary["Availability_Impact"]
        if "Access_Complexity" in dictionary:
            self.Access_Complexity = dictionary["Access_Complexity"]
        if "Authentication" in dictionary:
            self.Authentication = dictionary["Authentication"]
        if "Gained_Access" in dictionary:
            self.Gained_Access = dictionary["Gained_Access"]
        if "Vulnerability_type" in dictionary:
            self.Vulnerability_type = dictionary["Vulnerability_type"]
        if "CWE_ID" in dictionary:
            self.CWE_ID = dictionary["CWE_ID"]

    def __str__(self):
        return super(CVEDetails, self).__str__()


def get_command_line_arguments():
    return sys.argv[1:]


def build_URL_by_CVE_id(cveId):
    return ("https://www.cvedetails.com/cve/" + cveId)


def get_page_from_url(url):
    return requests.get(url)


def check_for_error(tree):
    error_divs = tree.find_class(ERROR_CLASS_NAME)
    if (len(error_divs) != 0):
        print ("Error:" + error_divs[0].text_content())
        return False
    return True

def parse_CVEDetails(tree):
    cv_details_dictionary = {}
    cv_details_dictionary["CVSS_Score"] = tree.xpath('//*[@id="cvssscorestable"]/tr[1]/td/div/text()')
    cv_details_dictionary["Confidentiality_Impact"] = tree.xpath('//*[@id="cvssscorestable"]/tr[2]/td/span[1]/text()')
    cv_details_dictionary["Integrity_Impact"] = tree.xpath("//*[@id=\"cvssscorestable\"]/tr[3]/td/span[1]/text()")
    cv_details_dictionary["Availability_Impact"] = tree.xpath("//*[@id=\"cvssscorestable\"]/tr[4]/td/span[1]")
    cv_details_dictionary["Access_Complexity"] = tree.xpath("//*[@id=\"cvssscorestable\"]/tr[5]/td/span[1]")
    cv_details_dictionary["Authentication"] = tree.xpath("//*[@id=\"cvssscorestable\"]/tr[6]/td/span[1]")
    cv_details_dictionary["Gained_Access"] = tree.xpath("//*[@id=\"cvssscorestable\"]/tr[7]/td/span")
    cv_details_dictionary["Vulnerability_type"] = tree.xpath("//*[@id=\"cvssscorestable\"]/tr[8]/td/span[1]")
    cv_details_dictionary["CWE_ID"] = tree.xpath('//*[@id="cvssscorestable"]/tr[9]/td')
    cv_details_dictionary["Products_affected"] = tree.xpath("//*[@id=\"vulnprodstable\"]")
    #it's a table
    cv_details_dictionary["Vendor"] = tree.xpath('//*[@id="addvendsuppdata"]/tr[2]/td[1]/a')
    cveDetails = CVEDetails(cv_details_dictionary)

    return cveDetails

if __name__ == "__main__":
    cve_id_list = get_command_line_arguments()

    if (len(cve_id_list) == 0):
        print ("Error.No argumnets passed. Pass at least one CVE id in script parameters")

    for cveId in cve_id_list:
        url = build_URL_by_CVE_id(cveId)
        page = get_page_from_url(url)
        # convert to html tree
        tree = html.fromstring(page.content)
        if(check_for_error(tree)):
            print (parse_CVEDetails(tree))


