// Функция для перевода текста в азбуку Морзе
function translate() {
    console.log('start')
    var inputText = document.getElementById("input-text").value;
    var outputText = "";

    // Определение азбуки Морзе
    var morseAlphabet = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
        "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
        "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..",
        "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
        ".": ".-.-.-", ",": "--..--", "?": "..--..", "'": ".----.", "!": "-.-.--", "/": "-..-.", "(": "-.--.", ")": "-.--.-", "&": ".-...",
        ":": "---...", ";": "-.-.-.", "=": "-...-", "+": ".-.-.", "-": "-....-", "_": "..--.-", "\"": ".-..-.", "$": "...-..-", "@": ".--.-.",
        " ": "/"
    };

    // Перевод текста в азбуку Морзе
    for (var i = 0; i < inputText.length; i++) {
        var char = inputText.charAt(i).toUpperCase();
        if (morseAlphabet[char]) {
            outputText += morseAlphabet[char] + " ";
        } else {
            outputText += char + " ";
        }
    }

    // Вывод перевода
    document.getElementById("output-text").value = outputText.trim();
}

// Привязка события клика к кнопке
document.getElementById("translate-btn").addEventListener("click", translate);