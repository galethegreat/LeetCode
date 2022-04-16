# [7, 4, 5, 4, 4, 2, 3]
# [7, 4, 5, 4, 4, 8, 3]

def numberOfPairs(heights):
	if len(heights) < 2:
    return 0
  num_of_pairs = 0
  heights_seen = list()
  heights_seen.append(heights[0]) #
  for height in heights[1:]:

    if height < heights_seen[-1]:
      num_of_pairs += 1
      heights_seen.append(height)

    else:
      while heights_seen and height >= heights_seen[-1]:
        if height != heights_seen[-1]:
        	num_of_pairs += 1#
        heights_seen.pop()
      if heights_seen:#
        num_of_pairs += 1
      heights_seen.append(height)

  return num_of_pairs
