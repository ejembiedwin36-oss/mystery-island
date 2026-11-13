
// ========================================
// MYSTERY ISLAND - THE LOST LIGHTHOUSE
// First mobile game scene
// ========================================

// Find the canvas from our HTML page.
const canvas = document.getElementById("game-canvas");

// Get the drawing tool.
const ctx = canvas.getContext("2d");

// Explorer's starting position.
let player = {
    x: 260,
    y: 260,
    step: 15
};

// Explorer's inventory.
let inventory = [];

// collecttion status of 

// Draw a palm tree.
function drawTree(x, y) {

    // Tree trunk.
    ctx.fillStyle = "#79502b";
    ctx.fillRect(x - 6, y, 12, 45);

    // Green leaves.
    ctx.fillStyle = "#176b3a";

    ctx.beginPath();
    ctx.arc(x, y - 8, 25, 0, Math.PI * 2);
    ctx.fill();

    ctx.beginPath();
    ctx.arc(x - 18, y + 2, 16, 0, Math.PI * 2);
    ctx.fill();

    ctx.beginPath();
    ctx.arc(x + 18, y + 2, 16, 0, Math.PI * 2);
    ctx.fill();
}


// Draw the lighthouse.
function drawLighthouse() {

    // Main tower.
    ctx.fillStyle = "#f4f1de";

    ctx.beginPath();
    ctx.moveTo(625, 180);
    ctx.lineTo(675, 180);
    ctx.lineTo(665, 310);
    ctx.lineTo(635, 310);
    ctx.closePath();
    ctx.fill();

    // Red stripes.
    ctx.fillStyle = "#c44536";
    ctx.fillRect(632, 220, 36, 15);
    ctx.fillRect(630, 270, 40, 15);

    // Lighthouse roof.
    ctx.fillStyle = "#8d2929";

    ctx.beginPath();
    ctx.moveTo(615, 180);
    ctx.lineTo(685, 180);
    ctx.lineTo(650, 145);
    ctx.closePath();
    ctx.fill();

    // Light room.
    ctx.fillStyle = "#ffd166";
    ctx.fillRect(638, 153, 24, 27);

    // Door.
    ctx.fillStyle = "#543b2a";
    ctx.fillRect(642, 280, 16, 30);
}


// Draw the rope item.
function drawRope(x, y) {

    // Rope colour.
    ctx.strokeStyle = "#79502b";
    ctx.lineWidth = 5;

    // Draw the coiled rope.
    ctx.beginPath();
    ctx.arc(x, y, 10, 0, Math.PI * 2);
    ctx.stroke();

    // Draw the rope end.
    ctx.beginPath();
    ctx.moveTo(x + 8, y + 5);
    ctx.lineTo(x + 18, y + 12);
    ctx.stroke();
}


// Draw the lantern item.
function drawLantern(x, y) {

    // Lantern handle.
    ctx.strokeStyle = "#333333";
    ctx.lineWidth = 3;
    ctx.strokeRect(x - 7, y - 15, 14, 5);

    // Lantern body.
    ctx.fillStyle = "#f4a261";
    ctx.fillRect(x - 9, y - 10, 18, 22);

    // Lantern light.
    ctx.fillStyle = "#ffd166";
    ctx.fillRect(x - 5, y - 6, 10, 14);

    // Lantern base.
    ctx.fillStyle = "#333333";
    ctx.fillRect(x - 11, y + 12, 22, 4);
}





// Draw the explorer.
function drawExplorer(x, y) {

    // Head.
    ctx.fillStyle = "#8d5524";
    ctx.beginPath();
    ctx.arc(x, y - 22, 12, 0, Math.PI * 2);
    ctx.fill();

    // Body.
    ctx.fillStyle = "#e76f51";
    ctx.fillRect(x - 10, y - 10, 20, 28);

    // Legs.
    ctx.fillStyle = "#263238";
    ctx.fillRect(x - 9, y + 18, 7, 15);
    ctx.fillRect(x + 2, y + 18, 7, 15);

    // Explorer's backpack.
    ctx.fillStyle = "#79502b";
    ctx.fillRect(x + 8, y - 8, 9, 17);
}


// Draw the complete island.
function drawWorld() {

    // Clear the canvas.
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Ocean.
    ctx.fillStyle = "#2389b8";
    ctx.fillRect(0, 0, 800, 450);

    // Ocean waves.
    ctx.strokeStyle = "#83d5e8";
    ctx.lineWidth = 3;

    for (let x = 20; x < 800; x += 100) {
        ctx.beginPath();
        ctx.arc(x, 80, 15, 0, Math.PI);
        ctx.stroke();
    }

    // Sandy island.
    ctx.fillStyle = "#e9c46a";
    ctx.beginPath();
    ctx.ellipse(400, 250, 360, 170, 0, 0, Math.PI * 2);
    ctx.fill();

    // Green grass.
    ctx.fillStyle = "#70a84b";
    ctx.beginPath();
    ctx.ellipse(400, 230, 280, 125, 0, 0, Math.PI * 2);
    ctx.fill();

    // Path to the lighthouse.
    ctx.strokeStyle = "#d6a85f";
    ctx.lineWidth = 30;
    ctx.lineCap = "round";

    ctx.beginPath();
    ctx.moveTo(260, 300);
    ctx.quadraticCurveTo(420, 350, 650, 300);
    ctx.stroke();

    // Trees.
    drawTree(170, 180);
    drawTree(260, 130);
    drawTree(510, 150);
    drawTree(550, 270);
    drawTree(350, 320);

    // Lighthouse.
    drawLighthouse();

    // Rope item.
    drawRope(130, 245);

    // Lantern item.
    drawLantern(700, 320);

    // Explorer.
    drawExplorer(player.x, player.y);

    // Island name.
    ctx.fillStyle = "#ffffff";
    ctx.font = "bold 20px Arial";
    ctx.fillText("MYSTERY ISLAND", 300, 55);
}


// Draw the island when the page loads.
drawWorld();


// Check whether a position is inside the sandy island.
function isInsideIsland(x, y) {

    // Calculate the horizontal distance from the island centre.
    let horizontal = (x - 400) / 345;

    // Calculate the vertical distance from the island centre.
    let vertical = (y - 250) / 155;

    // Return true if the position is inside the island.
    return (horizontal * horizontal) + (vertical * vertical) <= 1;
}


// Move the explorer in the chosen direction.

function movePlayer(xChange, yChange) {

    // Calculate the proposed position.
    let newX = player.x + xChange;
    let newY = player.y + yChange;

    // Check whether the proposed position is inside the island.
    if (isInsideIsland(newX, newY)) {

        // Accept the new position.
        player.x = newX;
        player.y = newY;
    }

    // Redraw the island.
    drawWorld();

    // Let's temporarily add a message
    console.log("Explorer position:", player.x, player.y);
}



// RIGHT button.
document.getElementById("move-right").addEventListener("click", function () {
    movePlayer(player.step, 0);
});


// LEFT button.
document.getElementById("move-left").addEventListener("click", function () {
    movePlayer(-player.step, 0);
});


// UP button.
document.getElementById("move-up").addEventListener("click", function () {
    movePlayer(0, -player.step);
});


// DOWN button.
document.getElementById("move-down").addEventListener("click", function () {
    movePlayer(0, player.step);
});

