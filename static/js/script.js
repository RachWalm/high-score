// Leaderboard functionality

// let allowedScores = JSON.parse(localStorage.getItem("allowedScores")) || []

// const score = document.getElementById("score");

// function getJson () {
    
//     fetch('./data/scores.json')
//     .then((response) => response.json())
//     .then((json) => console.log(json));
// }

// localStorage.setItem("sum_rank", JSON.stringify({sum_rank}));
localStorage.clear();
localStorage.setItem(("first", 2), ("thirst", 3))

// var sumRank = {{ sum_rank | tojson }};
// console.log(sumRank)
// var board = document.getElementById("leaderboard-list");
// var sum = {{ sum_rank | safe}}
// console.log(sum)
// for(var i = 0; i < test.length; i++) {
//     console.log(test);
//     var selection = document.createElement("OPTION"),
//     txt = document.createTextNode(test[i]);
//     selection.appendChild(txt);
//     selection.setAttribute("value", test[i]);
//     board.insertBefore(selection, board.lastChild)
// }