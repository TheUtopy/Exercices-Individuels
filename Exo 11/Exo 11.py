from flask import Flask, render_template, request

### Etape 1:

def decoupe_chaine(string):
    dic = {}
    x = 0
    for char_ind in range(len(string)):
        if char_ind + 1 < len(string) and string[char_ind] != string[char_ind+1]:
            dic.update({x:char_ind+1})
            x = char_ind+1
        elif char_ind +1 == len(string):
            dic.update({x:len(string)})

    new_string = ""
    for i in dic:
        new_string += string[i:dic[i]]
        if not list(dic)[-1] == i:
            new_string+= " "

    return new_string


# print(decoupe_chaine("aabbca"))

### Etape 2:

def decrit_chaine(string):
    dic = {}
    x = 0
    for char_ind in range(len(string)):
        if char_ind + 1 < len(string) and string[char_ind] != string[char_ind+1]:
            dic.update({x:char_ind+1})
            x = char_ind+1
        elif char_ind +1 == len(string):
            dic.update({x:len(string)})

    new_string = ""
    for i in dic:
        new_string += str(dic[i] - i) + string[i]

    return new_string

# print(decrit_chaine("aabbcaggghhttttt"))

### Etape 3:

def suite_conway(string, n):
    if n == 1:
        return string
    n -= 1
    print(string)
    string = decrit_chaine(string)
    return suite_conway(string, n)

# print(suite_conway("1", 3))

### Etape 4:

def suite_conway_tab(string, n, result=None):
    if result == None:
        result = []
    if n == 0:
        return result
    n -= 1
    result.append(string)
    string = decrit_chaine(string)
    suite_conway_tab(string, n, result)
    return result

# print(suite_conway_tab("aab", 4))


def html_result(tab):
    html_tab = ""
    for elem in tab:
        html_tab += "<p>" + elem + "</p><br>"

    return html_tab


app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("Exo 11.html")

@app.route("/result", methods=["POST", "GET"])
def result():
    output = request.form.to_dict()
    string = output["string"]
    n = output["n"]
    html_text = html_result(suite_conway_tab(string, int(n)))

    return render_template("Exo 11.html", html_text=html_text)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
