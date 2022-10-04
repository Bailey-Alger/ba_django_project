const adjectives = ["blind", "dirty", "gross", "giant",
    "nasty", "crazy", "magic", "upset",
    "brave", "super", "harsh", "smart",
    "rigid", "stiff", "eager", "fatal",
    "cruel", "noble", "crude", "solar",
    "toxic", "novel", "weird", "noisy",
    "sunny", "alien", "dense", "tense",
    "grave", "swift", "petty", "naive",
    "vocal", "sandy", "alert", "dusty",
    "shiny", "polar", "fancy", "weary",
    "rocky", "muddy", "frail", "moist",
    "merry", "fatty", "brisk", "fiery",
    "plump", "jolly", "shaky", "blunt",
    "witty", "micro", "stern", "curly",
    "hairy", "viral", "dizzy", "tasty",
    "stout", "pious", "messy", "hefty",
    "bulky", "stray", "hasty", "sleek",
    "stone", "regal", "eerie", "macho",
    "timid", "misty", "shady", "amber",
    "lunar", "adept", "silky", "lowly",
    "aloof", "lousy", "manic", "scary",
    "snowy", "moody", "spicy", "lucid",
    "leafy", "smoky", "slick", "husky",
    "gaunt", "juicy", "sonic", "fuzzy"];

const animals = ["ant", "hawk", "eagle", "cat",
    "chicken", "rooster", "cow", "bull",
    "dog", "elephant", "trout", "fox",
    "horse", "lion", "monkey", "penguin",
    "pig", "boar", "rabbit", "bunny",
    "sheep", "ram", "tiger", "whale",
    "wolf", "alligator", "wasp", "shark"];

function getRandomInt(max) {
    return Math.floor(Math.random() * max);
}

function createBtn(request) {
    let adj = adjectives[getRandomInt(adjectives.length)];
    let animal = animals[getRandomInt(animals.length)];
    let usern = adj + "-" + animal;
    let passw = animal + getRandomInt(100);
    let account = "username: " + usern + "&nbsp &nbsp &nbsp &nbsp password: " + passw;
    document.getElementById("accountinfo").innerHTML = account;
}