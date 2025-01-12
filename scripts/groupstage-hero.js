const dataHeroStats = document.querySelector('#hero-stats tbody');

function displayDataInTable(data) {
    data.forEach(item => {
        const row = document.createElement('tr');
        row.innerHTML = `
        <td>${item.id}</td>
        <td>${item.name}</td>
        <td>${item.total}</td>
        <td>${item.wins}</td>
        <td>${item.losses}</td>
        <td>${item.wr}</td>
        <td>${item.t}</td>
        <td>${item.r_total}</td>
        <td>${item.r_wins}</td>
        <td>${item.r_losses}</td>
        <td>${item.r_wr}</td>
        <td>${item.d_total}</td>
        <td>${item.d_wins}</td>
        <td>${item.d_losses}</td>
        <td>${item.d_wr}</td>
        <td>${item.bans}</td>
        <td>${item.bans_t}</td>
        <td>${item.total_pick_ban}</td>
        <td>${item.p_b_t}</td>
    `;
        dataHeroStats.appendChild(row);
    });
}

fetch('data/groupstage-hero.json') // Lokasi file JSON
    .then(response => {
        if (!response.ok) {
            throw new Error('Gagal mengambil data: ' + response.statusText);
        }
        return response.json();
    })
    .then(data => displayDataInTable(data))
    .catch(error => {
        console.error('Error:', error);
    });