from entity.user import User

class REA(User):

    def __init__(self, userID, username, password, email, active):
        super().__init__(userID, username, password, email, 2, active)
    
    # 15. Create new property listings
    def createListing(self, newPropertyDetails):
        """Inserts a property listing into database"""
        if not newPropertyDetails or len(newPropertyDetails) != 4:
            return False  # Input validation failed
        try:
            # f"NULL, '{p_name}', '{location}', '{description}', '{img_name}', {price}, {rea_id}, {seller_id}, {sold_buyer}, {view_count}, {wishlisted}"
            details = f"NULL, '{newPropertyDetails[0]}', '{newPropertyDetails[1]}', 'Test', '{newPropertyDetails[2]}', {newPropertyDetails[3]}, {self.userID}, 0, -1, 0, 0"
            REA.db.insert_into_table("Property", details)
            return True

        except Exception as e:
            print(f"Error creating listing: {e}")
            return False

    # 16. View existing property listings
    def viewListing(self, p_id = "") -> list:
        """View Listing by ID"""
        if p_id == "": # View all accounts
            search_result = REA.db.view_table("Property")
            return list(search_result)
        else:
            search_param =  f"id ='{p_id}'"
            search_result = REA.db.search_one("Property", search_param=search_param)
            return list(search_result)
        
    def updateViewCount(self, pl):
        """ Increments the view count of a property by one when selected """
        p_id = pl[0]
        updated_p_view_count = pl[-2] + 1
        REA.db.update_table("Property", f"view_count = {updated_p_view_count}", f"id = {p_id}")


    # 17. Update property listings
    def update_listing(self, entered_details):
        target_property = REA.db.search_one("Property", f"p_name = '{entered_details[0]}'")
        if target_property:
            update_details = ""
            # Update target_account with remaining information
            REA.db.update_table("Property", update_details, f"p_name = '{entered_details[0]}'")
            return True
        else:
            return False

    # 18. Delete property listings
    def delete_listing(self, p_id):
        """Delete property listing"""
        target_property  = REA.db.search_one("Property", f"p_id = {p_id}")
        if target_property:
            REA.db.delete_from_table("Property", f"p_id = {p_id}")
            return True
        else:
            return False

    


    
