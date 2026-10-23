# TOPS Session 5: Lists, list methods, and tuple immutability

playlist_ids = [101, 205, 309, 412, 518]
print("Original playlist:", playlist_ids)

playlist_ids.append(620)
playlist_ids.extend([711, 812])
print("Updated playlist:", playlist_ids)

removed_id = playlist_ids.pop()
print("Removed ID:", removed_id)
print("Remaining playlist:", playlist_ids)

insta_filters = ("Clarendon", "Juno", "Lark", "Gingham")
print("Instagram filters:", insta_filters)

# Tuples are immutable. The following would raise TypeError:
# insta_filters[0] = "New Filter"

# Lists can be changed; tuples are useful for fixed collections.
recent_orders = ["Order-101", "Order-102", "Order-103"]
fixed_ipl_teams = ("Titans", "Royals", "Super Kings")
print("Use a list for changing orders:", recent_orders)
print("Use a tuple for fixed team names:", fixed_ipl_teams)
