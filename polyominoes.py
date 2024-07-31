# Start with polyominoes with every point on the top row.
# Store the polyominoes as a list of points.
polyominoes = [frozenset([(i, 0)]) for i in range(5)]


while polyominoes:
  points = polyominoes.pop(0)

  # Only print if there is a # in the first column (otherwise there would be leading whitespace)
  # Note: If there's leading whitespace, there is guaranteed to be an equivalent polyomino without leading whitespace
  if any(x == 0 for x, _ in points):
    grid = [[' '] * 6 for _ in range(6)]
    for x, y in points:
      grid[x][y] = '#'
    print('\n'.join(''.join(x).rstrip(' ') for x in grid).rstrip('\n') + '\n')

  # If it's already size 6, it's maximal size, so we don't need to generate any more polyominoes from it.
  if len(points) == 6:
    continue

  # Loop over every point in the polyomino
  for x, y in points:
    # Loop over all of its neighbors, to find a point that can be added
    for x1, y1 in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]:
      # Make sure it's within bounds and not already in the polyomino
      if 0 <= x1 < 6 and 0 <= y1 < 6 and (x1, y1) not in points:
        new_points = points | frozenset([(x1, y1)])
        if new_points not in polyominoes:
          polyominoes.append(new_points)
