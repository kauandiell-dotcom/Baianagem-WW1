import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import france_builder.build_foci_list as b
import france_builder.wing3_foci as w3
import france_builder.wing4_foci as w4
import france_builder.wing5_foci as w5

def run_check():
    all_foci = b.main() + w3.get_wing_3_foci() + w4.get_wing_4_foci() + w5.get_wing_5_foci()
    print(f"Total Foci loaded: {len(all_foci)}")

    id_map = {f['id']: f for f in all_foci}

    if len(id_map) != len(all_foci):
        print("WARNING: Duplicate IDs exist!")

    # Check coords
    coords = {}
    collisions = []
    for f in all_foci:
        pt = (f['x'], f['y'])
        if pt in coords:
            collisions.append((pt, f['id'], coords[pt]['id']))
        coords[pt] = f

    if collisions:
        print(f"COLLISIONS: {len(collisions)}")
        for c in collisions:
            print("  ", c)
    else:
        print("Zero coordinate collisions! All (x, y) coordinates unique.")

    # Check prereqs
    missing_p = []
    bad_dy = []
    for f in all_foci:
        for p in f.get('prereq', []):
            if isinstance(p, list):
                for sub_p in p:
                    if sub_p not in id_map:
                        missing_p.append((f['id'], sub_p))
                    elif f['y'] <= id_map[sub_p]['y']:
                        bad_dy.append((f['id'], sub_p, f['y'], id_map[sub_p]['y']))
            else:
                if p not in id_map:
                    missing_p.append((f['id'], p))
                elif f['y'] <= id_map[p]['y']:
                    bad_dy.append((f['id'], p, f['y'], id_map[p]['y']))

    if missing_p:
        print(f"MISSING PREREQS: {len(missing_p)}")
        for mp in missing_p:
            print("  ", mp)
    else:
        print("All prerequisites exist in id_map!")

    if bad_dy:
        print(f"BAD DY (child.y <= parent.y): {len(bad_dy)}")
        for bd in bad_dy:
            print("  ", bd)
    else:
        print("All dy >= 1 strictly satisfied!")

    # Check mut_ex
    missing_m = []
    for f in all_foci:
        for m in f.get('mut_ex', []):
            if m not in id_map:
                missing_m.append((f['id'], m))
    if missing_m:
        print(f"MISSING MUT_EX: {len(missing_m)}")
        for mm in missing_m:
            print("  ", mm)
    else:
        print("All mutually_exclusive IDs exist!")

if __name__ == "__main__":
    run_check()
