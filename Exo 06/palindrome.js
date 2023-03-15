// Etape 1

function isValidDate(date) {
    date = date.split("/")
    if (!maxDaysInMonth(date[0], date[1]) || date[2] < 1000 || date[2] > 9999) {
        return false
    }
    return true
}

function maxDaysInMonth(days, month) {
    if (["01", "03", "05", "07", "08", "10", "12"].includes(month) && parseInt(days) <= 31) {
        return true
    }
    else if (["04", "06", "09", "11"].includes(month) && parseInt(days) <= 30) {
        return true
    }
    else if (month == 02 && parseInt(days) <= 29) {
        return true
    }
    else {
        return false
    }
}

// Etape 2

// function isPalindrome(date) {
//     date = date.replace("/", "")
//     date = date.split("/")
//     date[0] = date[0][3] + date[0][2] + date[0][1] + date[0][0]
//     if (date[0] == date[1]) {
//         return true
//     }
//     return false
// }

//Etape 3

function getNextPalindromes(x) {
    let date = "15/03/2023"
    let result = []
    let separated_date = date.split("/")
    let truc
    while (x > 0) {
        if (isValidDate(separated_date.join("/"))) {
            truc = separated_date[1][1] + separated_date[1][0] + separated_date[0][1] + separated_date[0][0]
            if (separated_date[2] == truc) {
                result.push(separated_date.join("/"))
                x -= 1
            }
        }
        if (parseInt(separated_date[2][3]) >= 2) {
            if (separated_date[2][2] == "9") {
                if (separated_date[2][1] == "9") {
                    separated_date[2] = String(parseInt(separated_date[2][0]) + 1) + "000"
                } else {
                    separated_date[2][1] = separated_date[2][0] + String(parseInt(separated_date[2][1]) + 1) + "00"
                }
            } else {
                separated_date[2] = separated_date[2][0] + separated_date[2][1] + String(parseInt(separated_date[2][2]) + 1) + "0"
            }
        } else {
            separated_date[2] = separated_date[2][0] + separated_date[2][1] + separated_date[2][2] + String(parseInt(separated_date[2][3]) + 1)
        }
        separated_date[0] = separated_date[2][3] + separated_date[2][2]
        separated_date[1] = separated_date[2][1] + separated_date[2][0]
    }
    return result
}

// Etape 04

function isPalindrome(text) {
    let left_text = ""
    let half_length
    if (text.length % 2 == 1) {
        half_length = (text.length - 1) / 2
        for (let i = 0; i < half_length; i++) {
            left_text = text[i] + left_text
        }
        half_length = (text.length + 1) / 2
    } else {
        half_length = text.length / 2
        for (let i = 0; i < half_length; i++) {
            left_text = text[i] + left_text
        }
    }
    if (left_text == text.slice(half_length, text.length)) {
        return true
    } else {
        return false
    }
}

function isDatePalindrome(date) {
    if (isValidDate(date)) {
        date = date.replaceAll("/", "")
        if (isPalindrome(date)) {
            return "This date is a palindrome."
        } else {
            return "This date is not a palindrome."
        }
    } else {
        return "Date not valid."
    }
}

console.log(isDatePalindrome("11/02/2011"))