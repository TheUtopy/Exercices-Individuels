// Etape 1

function sapin1(num) {
    console.log(" ".repeat(num + 1) + "+")
    const firstFloorLength = num * 2 + 3
    for (let i = num; i >= 0; i--) {
        console.log(" ".repeat(i) + "/" + "*".repeat(firstFloorLength - ((i + 1) * 2)) + "\\" + " ".repeat(i))
    }
}

//sapin1(2)

// Etape 2

function sapin2(num) {
    const space = numberOfSpace(num)
    console.log(" ".repeat(num + 1) + "+")
    const firstFloorLength = maxWidth(num)
    for (let i = num; i >= 0; i--) {
        console.log(" ".repeat(i) + "/" + "*".repeat(firstFloorLength - ((i + 1) * 2)) + "\\")
    }
}

function numberOfSpace(num) {
    x = maxWidth(num)
    let space = (x - 3) / 2
    return space
}

function maxWidth(num, result = 4) {
    if (num == 1) {
        return result + 1
    }
    if (num % 3 == 0) {
        num--
        return maxWidth(num, result)
    } else {
        num--
        result += 2
        return maxWidth(num, result)
    }
}

console.log(maxWidth(15))
sapin2(3)

// 5 7 7 9 11 11 13