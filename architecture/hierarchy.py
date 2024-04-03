page_hierarchy = {
    "home": 0,

    "overview-on-conducting-a-study": {
        "parent": "home", 
        "display": "Overview on Conducting a Study"
        },
    "create-a-new-study": {
        "parent": "overview-on-conducting-a-study", 
        "display": "Create a New Study"
        },
        "Select_the_Study_Type": {
            "parent": "Create_a_New_Study", 
            "display": "Select the Study Type"
            },
            
        "Fill_in_the_Study_Information": {
            "parent": "Create_a_New_Study", 
            "display": "Fill in the Study Information"
            },

            "Study_Name": {
                "parent": "Fill_in_the_Study_Information", 
                "display": "Study Name"
                },
            "Brief_Abstract": {
                "parent": "Fill_in_the_Study_Information", 
                "display": "Brief Abstract"
                },
            "Detailed_Description": {
                "parent": "Fill_in_the_Study_Information", 
                "display": "Detailed Description"
                },
            "Eligibility_Requirements": {
                "parent": "Fill_in_the_Study_Information", 
                "display": "Eligibility Requirements"
                },
            "Duration": {
                "parent": "Fill_in_the_Study_Information", 
                "display": "Duration"
                },
            "Preparation": {
                "parent": "Fill_in_the_Study_Information", 
                "display": "Preparation"
                },
            "Duration": {
                "parent": "Fill_in_the_Study_Information", 
                "display": "Duration"
                },
            "Ethical_Approval": {
                "parent": "Fill_in_the_Study_Information", 
                "display": "Ethical Approval"
                },
            
}

def build_full_breadcrumb_path(page_hierarchy):
    full_paths = {}

    def build_path(page_name):
        # Base case: if this page is the "home" page or has no parent defined
        if page_hierarchy[page_name] == 0:
            return [{"name": "home", "display": "Home"}]

        page_info = page_hierarchy[page_name]
        parent_path = build_path(page_info["parent"]) if page_info["parent"] in page_hierarchy else []
        current_page_path = {"name": page_name, "display": page_info["display"]}
        return parent_path + [current_page_path]

    for page in page_hierarchy:
        full_paths[page] = build_path(page)

    return full_paths

# Transform the simplified hierarchy into the full breadcrumb paths
full_page_hierarchy = build_full_breadcrumb_path(page_hierarchy)


