const url = 'https://s6stno05x0.execute-api.us-east-1.amazonaws.com/Test/VisitorCounter/visit';
      const data = { test: 'event' };
      const options = {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      };

      fetch(url, options)
        .then(response => response.json())
        .then(data => {
          const result = document.getElementById('result');
          result.textContent = data.body;
        })
        .catch(error => console.error(error));


