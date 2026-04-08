const employees = [
    { name: "Sarah Jenkins", dept: "Engineering", risk: 0.92, factor: "Promotion Stagnation" },
    { name: "Michael Ross", dept: "Sales", risk: 0.85, factor: "Salary vs Market Gap" },
    { name: "Emily Zhao", dept: "Product", risk: 0.78, factor: "Low Engagement Score" },
    { name: "David Miller", dept: "IT Support", risk: 0.55, factor: "Commute Distance" },
    { name: "Anna Schmidt", dept: "Engineering", risk: 0.22, factor: "Healthy Engagement" }
];

function renderRiskList() {
    const list = document.getElementById('risk-list');
    list.innerHTML = employees.map(emp => {
        const riskClass = emp.risk > 0.7 ? 'risk-high' : (emp.risk > 0.4 ? 'risk-med' : 'risk-low');
        const riskLabel = emp.risk > 0.7 ? 'High' : (emp.risk > 0.4 ? 'Medium' : 'Low');
        
        return `
            <div class="employee-row">
                <div>
                    <strong>${emp.name}</strong><br>
                    <span style="font-size: 0.8rem; color: var(--text-secondary)">${emp.dept}</span>
                </div>
                <div class="risk-tag ${riskClass}">${riskLabel} (${(emp.risk * 100).toFixed(0)}%)</div>
                <div style="font-size: 0.8rem; color: var(--text-secondary)">Primary Driver: ${emp.factor}</div>
                <div style="text-align: right">
                    <button class="btn-action" onclick="alert('Strategy Generated: ${recommendAction(emp)}')">Generate Strategy</button>
                </div>
            </div>
        `;
    }).join('');
}

function recommendAction(emp) {
    if (emp.factor === "Promotion Stagnation") return "Career Development Track & Title Review";
    if (emp.factor === "Salary vs Market Gap") return "15% Base Increase & Performance Bonus";
    if (emp.factor === "Low Engagement Score") return "Mental Health Check-in & Manager 1:1";
    if (emp.factor === "Commute Distance") return "Remote Work Approval (3 days/week)";
    return "Positive Feedback Loop & Mentorship Role";
}

document.addEventListener('DOMContentLoaded', renderRiskList);
