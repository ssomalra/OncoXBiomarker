document.addEventListener("DOMContentLoaded", function () {
    const ctx = document.getElementById('biomarkerBarChart');
    if (!ctx) return;
  
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['Lung', 'Colorectal', 'Breast', 'Ovarian', 'Prostate', 'Skin'],
        datasets: [{
          data: [11, 8, 6, 9, 35, 28], // You can replace these with dynamic values if needed
          backgroundColor: [
            '#f7c32e', '#6c88f0', '#f7a6d6', '#00bfae', '#a4c4f3', '#8f8f8f'
          ],
          borderWidth: 1
        }]
      },
      options: {
        plugins: {
          legend: {
            display: false
          }
        },
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    });
  });
