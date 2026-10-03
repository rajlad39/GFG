class Solution:
    def formCoils(self, n):
        size = 4 * n
        total_elements = 8 * n * n

        # Helper function to generate a spiral coil
        def build_coil(start_r, start_c, dirs):
            coil = []
            r, c = start_r, start_c

            # Step sizes sequence: (size - 1), (size - 2), (size - 2), (size - 4), (size - 4), ...
            steps = [size - 1]
            curr_step = size - 2
            while curr_step > 0:
                steps.append(curr_step)
                steps.append(curr_step)
                curr_step -= 2

            dir_idx = 0
            # Add initial element
            coil.append(r * size + c + 1)

            # Follow spiral movement steps
            for move_count in steps:
                dr, dc = dirs[dir_idx % 4]
                for _ in range(move_count):
                    if len(coil) >= total_elements:
                        break
                    r += dr
                    c += dc
                    coil.append(r * size + c + 1)

                if len(coil) >= total_elements:
                    break
                dir_idx += 1

            return coil

        # Coil 1: Starts at (0, 0), moves Down, Right, Up, Left...
        dirs1 = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        coil1 = build_coil(0, 0, dirs1)

        # Coil 2: Starts at (size-1, size-1), moves Up, Left, Down, Right...
        dirs2 = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        coil2 = build_coil(size - 1, size - 1, dirs2)

        return [coil1, coil2]
        