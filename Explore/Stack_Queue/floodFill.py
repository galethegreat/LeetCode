class Solution:
    def floodFill(self, image, sr, sc, newColor):
        def neighbours(pixel, stack, visited, image, current_color):
            r, c = pixel[0], pixel[1]

            if r - 1 >= 0 and (r-1,c) not in visited and image[r-1][c] == current_color:
                stack.append((r-1,c))

            if c - 1 >= 0 and (r,c-1) not in visited and image[r][c-1] == current_color:
                stack.append((r,c-1))

            if r + 1 < len(image) and (r+1,c) not in visited and image[r+1][c] == current_color:
                stack.append((r+1,c))

            if c + 1 < len(image[0]) and (r,c+1) not in visited and image[r][c+1] == current_color:
                stack.append((r,c+1))

        if len(image) < 1 :return image
        if len(image[0]) < 1:return image

        stack = list()
        area = list()
        visited = set()
        current_color = image[sr][sc]

        stack.append((sr,sc))

        while len(stack) > 0 :

            pixel = stack.pop()

            visited.add(pixel)
            area.append(pixel)

            neighbours(pixel,stack,visited,image,current_color)

        for pixel in area:
            image[pixel[0]][pixel[1]] = newColor

        return image

image = [[0,0,0],[0,0,0]]
sr = 0
sc = 0
newColor = 2
print(Solution().floodFill(image,sr,sc,newColor))
