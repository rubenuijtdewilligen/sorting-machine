<script>
  import '@carbon/charts-svelte/styles.css';
  import { PieChart, LineChart } from '@carbon/charts-svelte';

  export let data;

  // Data for pie chart
  let class1count = 0;
  let class2count = 0;

  data.records.forEach((record) => {
    if (record.class === '1') class1count++;
    if (record.class === '2') class2count++;
  });

  // Data for line chart
  let lineChartData = [];

  const groupedRecords = data.records.reduce((accumulator, current) => {
    const date = new Date(current.created);
    date.setHours(0, 0, 0, 0);
    const group = `Class ${current.class}`;
    const key = `${group}-${date.toISOString()}`;

    if (!accumulator[key]) {
      accumulator[key] = {
        group,
        date,
        value: 0
      };
    }

    accumulator[key].value += 1;

    return accumulator;
  }, {});

  for (const key in groupedRecords) {
    if (groupedRecords.hasOwnProperty(key)) {
      lineChartData.push(groupedRecords[key]);
    }
  }

  lineChartData.sort((a, b) => a.date - b.date);
</script>

<h1 class="title text-2xl font-bold">Sorting Machine Statistics</h1>

<PieChart
  data={[
    {
      group: 'Class 1',
      value: class1count
    },
    {
      group: 'Class 2',
      value: class2count
    }
  ]}
  options={{
    title: 'Amount of chilli peppers per class',
    resizable: true,
    height: '400px'
  }}
/>

<hr class="mb-12 mt-12" />

<LineChart
  data={lineChartData}
  options={{
    title: 'Amount of chilli peppers per class per day',
    axes: {
      bottom: {
        title: 'Date',
        mapsTo: 'date',
        scaleType: 'time'
      },
      left: {
        mapsTo: 'value',
        title: 'Chilli peppers',
        scaleType: 'linear'
      }
    },
    curve: 'curveMonotoneX',
    height: '500px'
  }}
/>
