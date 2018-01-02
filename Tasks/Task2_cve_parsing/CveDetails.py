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
    Vendor = ""

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
        if "Vendor" in dictionary:
            self.Vendor = dictionary["Vendor"]

    def __str__(self):
        return format("""
    CWE ID:{} ,
    CVSS Score: {}
    Confidentiality_Impact: {}
    Integrity_Impact: {}
    Availability_Impact: {}
    Access_Complexity: {}
    Authentication: {}
    Gained_Access: {}
    Vulnerability_type: {}
    Vendor: {}""".format(self.CWE_ID, self.CVSS_Score, self.Confidentiality_Impact
                         , self.Integrity_Impact, self.Availability_Impact,
                         self.Access_Complexity, self.Authentication, self.Gained_Access, self.Vulnerability_type,
                         self.Vendor))
