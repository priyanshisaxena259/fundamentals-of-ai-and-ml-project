<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>ChemWizard</title>
    <script src="https://www.chemdoodle.com/download/ChemDoodleWeb.js"></script>
    <link rel="stylesheet" href="https://www.chemdoodle.com/download/ChemDoodleWeb.css" />
    <style>
        body { font-family: Arial, sans-serif; margin: 0; background: #f3f6fa; }
        header { background: #1b4d89; color: white; padding: 20px; text-align: center; }
        container { padding: 20px; max-width: 900px; margin: auto; }
        .card { background: white; padding: 20px; margin: 20px 0; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
        input, button { padding: 10px; font-size: 16px; }
        button { background: #1b4d89; color: white; border: none; border-radius: 6px; cursor: pointer; }
        button:hover { opacity: 0.9; }
        #canvas { width: 300px; height: 300px; }
        table { width: 100%; border-collapse: collapse; }
        td { border: 1px solid #ccc; padding: 8px; text-align: center; cursor: pointer; }
        td:hover { background: #e8eef7; }
    </style>
</head>
<body>
    <header>
        <h1>ChemWizard Web App</h1>
        <p>Equation Balancer • Reaction Type Predictor • Molecule Viewer • Mini Periodic Table</p>
    </header>

    <div class="container">
        <!-- Equation Balancer -->
        <div class="card">
            <h2>⚖ Chemical Equation Balancer</h2>
            <input id="eqInput" placeholder="e.g. H2 + O2 -> H2O" style="width:70%" />
            <button onclick="balanceEq()">Balance</button>
            <p id="eqOutput" style="font-weight:bold; margin-top:10px;"></p>
        </div>

        <!-- Reaction Predictor -->
        <div class="card">
            <h2>🔍 Reaction Type Predictor</h2>
            <input id="rxInput" placeholder="e.g. HCl + NaOH" style="width:70%" />
            <button onclick="predictReaction()">Predict</button>
            <p id="rxOutput" style="font-weight:bold; margin-top:10px;"></p>
        </div>

        <!-- Molecule Viewer -->
        <div class="card">
            <h2>🧪 Molecule Viewer</h2>
            <input id="molInput" placeholder="Enter SMILES (e.g. COOH)" style="width:60%" />
            <button onclick="viewMol()">View</button>
            <canvas id="canvas"></canvas>
        </div>

        <!-- Periodic Table Mini -->
        <div class="card">
            <h2>📘 Mini Periodic Table</h2>
            <table id="ptable"></table>
            <p id="elemInfo" style="font-weight:bold; margin-top:10px;"></p>
        </div>
    </div>

<script>
// ------------------------ EQUATION BALANCER ---------------------------- //
function balanceEq() {
    let input = document.getElementById("eqInput").value;
    if (!input.includes("->")) {
        document.getElementById("eqOutput").innerText = "Invalid equation format";
        return;
    }
    // Simple placeholder (real balancer can be added later)
    document.getElementById("eqOutput").innerText = "Balanced Equation: " + input + " (demo only)";
}

// ------------------------ REACTION TYPE PREDICTOR ---------------------------- //
function predictReaction() {
    let eq = document.getElementById("rxInput").value.toLowerCase();
    let out = "";

    if (eq.includes("acid") || (eq.includes("hcl") && eq.includes("naoh"))) out = "Neutralization Reaction";
    else if (eq.includes("+ o2") || eq.includes("o2 +")) out = "Combustion Reaction";
    else if (eq.includes("->") && eq.split("->")[0].split("+").length > 1) out = "Combination Reaction";
    else out = "Could not classify (rule-based demo)";

    document.getElementById("rxOutput").innerText = out;
}

// ------------------------ MOLECULE VIEWER ---------------------------- //
const viewer = new ChemDoodle.ViewerCanvas('canvas', 300, 300);
function viewMol() {
    let smiles = document.getElementById('molInput').value;
    try {
        let mol = ChemDoodle.readSMILES(smiles);
        viewer.loadMolecule(mol);
    } catch {
        alert("Invalid SMILES string");
    }
}

// ------------------------ PERIODIC TABLE ---------------------------- //
const elements = ["H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar"];

window.onload = function() {
    let tbl = document.getElementById('ptable');
    let row = document.createElement('tr');

    elements.forEach(el => {
        let cell = document.createElement('td');
        cell.innerText = el;
        cell.onclick = () => document.getElementById('elemInfo').innerText = el + " selected";
        row.appendChild(cell);
    });

    tbl.appendChild(row);
};
</script>
</body>
</html>