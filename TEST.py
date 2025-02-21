alpha = list("ABCDEFGHIKLMNOPQRSTUVWXYZ")

pt = self.bifid_left_text.toPlainText().replace(" ", "").upper().replace("J", "I")
key = self.bifid_keyword.text().upper().replace(" ", "").replace("J", "I")
matrix_content = []
for char in key:
    if char in alpha and char not in matrix_content:  # because we dont have J in our bifid alpahbet since 5x5
        matrix_content.append(char)
for char in alpha:
    if char not in matrix_content:
        matrix_content.append(char)

matrix = []
index = 0
for rows in range(5):
    row = []
    for columns in range(5):
        row.append(matrix_content[index])
        index += 1
    matrix.append(row)
loc = []
for letter in pt:  # getting coordininates of the letters
    b = [(ix + 1, iy + 1) for ix, row in enumerate(matrix) for iy, i in enumerate(row) if i == letter]
    loc.append(b[0])
final = [(str(i[0]), str(i[1])) for i in loc]
final = ["".join(i) for i in final]
final = "".join(final)
rows = final[:int(len(final) / 2)]
cols = final[int(len(final) / 2):]
plainText = ""

for i in range(len(rows)):
    plainText += matrix[int(rows[i]) - 1][int(cols[i]) - 1]
self.bifid_right_text.setText(plainText)
self.btn_bifid_decrypt.clicked.connect(lambda:decrypt(self))