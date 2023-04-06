# Use the set f_suburbs as given as your starting point. Then,
# 1. Remove all suburbs that don't start with a F
# 2. Ensure that the suburbs listed below are in your set
#         Fairfield
#         Fairfield East
#         Fairfield Heights
#         Fairfield West
#         Fairlight
#         Fiddletown
#         Five Dock
#         Flemington
#         Forest Glen
#         Forest Lodge
#         Forestville
#         Freemans Reach
#         Frenchs Forest
#         Freshwater

f_suburbs = {"Randwick", "Kensington", "Frenchs Forest", "Flemington"}

nf_suburbs = []

for key in f_suburbs:
    if key[0] != 'F':
        nf_suburbs.append(key)

for suburb in nf_suburbs:
    f_suburbs.remove(suburb)

f_suburbs.update({
    'Fairfield',
    'Fairfield East',
    'Fairfield Heights',
    'Fairfield West',
    'Fairlight',
    'Fiddletown',
    'Five Dock',
    'Flemington',
    'Forest Glen',
    'Forest Lodge',
    'Forestville',
    'Freemans Reach',
    'Frenchs Forest',
    'Freshwater',
})
