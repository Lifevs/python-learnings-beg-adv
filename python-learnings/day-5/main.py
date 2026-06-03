distance_mi = 0
is_raining = False
has_bike = False
has_car = False
has_ride_share_app = False

if not distance_mi:
    # distance_mi is falsy (0, None, etc.)
    print(False)
elif distance_mi <= 1:
    # 1 mile or less: commute only if it is NOT raining
    if not is_raining:
        print(True)
    else:
        print(False)
elif distance_mi <= 6:
    # between 1 (excluded) and 6 (included)
    # commute only if has bike AND not raining
    if has_bike and not is_raining:
        print(True)
    else:
        print(False)
else:
    # distance_mi > 6
    if has_car or has_ride_share_app:
        print(True)
    else:
        print(False)
