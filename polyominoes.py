polyominoes = []

# Start with polyominoes with every point on the top row.
for i in range(5):
  grid = [[' '] * 6 for _ in range(6)]
  grid[0][i] = '#'
  polyominoes.append(grid)


while polyominoes:
  grid = polyominoes.pop(0)

  # Only print if there is a # in the first column (otherwise there would be leading whitespace)
  if any(x[0] == '#' for x in grid):
    print('\n'.join(''.join(x) for x in grid).rstrip() + '\n')
  
  # If it's already size 6, it's maximal size, so we don't need to generate any polyominoes from it.
  if sum(x.count('#') for x in grid) == 6:
    continue

  # Loop over every # in the polyomino
  for i0, row in enumerate(grid):
    for j0 in range(6):
      if row[j0] == ' ':
        continue

      # Loop over all of its neighbors, to find a point that can be added
      for i1, j1 in [(i0, j0 - 1), (i0, j0 + 1), (i0 - 1, j0), (i0 + 1, j0)]:
        # Make sure it's within bounds and not already a #
        if 0 <= i1 < 6 and 0 <= j1 < 6 and grid[i1][j1] == ' ':
          grid2 = [x[:] for x in grid]
          grid2[i1][j1] = '#'
          if grid2 not in polyominoes:
            polyominoes.append(grid2)
