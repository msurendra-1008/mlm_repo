from accounts.models import Profile

'''
Here all the code will help to excute the function for the views.py file
'''

# making helper function to create tree structure for UPA tree

def build_tree(user, level=0):
    tree = {
        'user': user,
        'level': level,
        'left_leg': None,
        'middle_leg': None,
        'right_leg': None,
    }
    
    profile = user.profile
    if profile.left_branch and profile.left_upa:
        tree['left_leg'] = build_tree(profile.left_upa, level+1)
    if profile.middle_branch and profile.middle_upa:
        tree['middle_leg'] = build_tree(profile.middle_upa, level+1)
    if profile.right_branch and profile.right_upa:
        tree['right_leg'] = build_tree(profile.right_upa, level+1)
        
    return tree
