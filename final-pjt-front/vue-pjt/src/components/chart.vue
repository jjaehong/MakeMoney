<template>
    <div style="text-align: center;">{{ day }}개월 금리에 따른 그래프</div>
    <Bar :data="chartData" :options="chartOptions" />
  </template>
  <script>
  import { Bar } from 'vue-chartjs'
  import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
  
  ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)
  
  export default {
  props: ['name', 'data1', 'data2', 'day'],
  name: 'BarChart',
  components: { Bar },
  data() {
    const minDataValue = Math.min(...this.data1, ...this.data2);
    const maxDataValue = Math.max(...this.data1, ...this.data2);

    return {
      chartData: {
        labels: this.name,
        datasets: [
          {
            label: '저축 금리',
            backgroundColor: '#f87979',
            data: this.data1,
          },
          {
            label: '최고 우대 금리',
            backgroundColor: 'rgba(255, 206, 86, 1)',
            data: this.data2,
          },
        ],
      },
      chartOptions: {
        scales: {
          x: {
            ticks: {
              maxRotation: 45, // Adjust the rotation angle as needed
              minRotation: 45,
            },
          },
          y: {
            suggestedMin: minDataValue,
            suggestedMax: maxDataValue,
          },
        },
      },
    };
  },
};
  </script>