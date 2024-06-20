const apiUrl = "http://0.0.0.0:8000/"
const colors = ['#6b40d84d', '#68de7a66', '#f4ac3666', '#ef414666', '#27b5ea66']

document.getElementById('inputText').addEventListener('input', () => {
    document.getElementById('inputText').style.borderColor = '';
});

document.getElementById('modelSelection').addEventListener('change', () => {
    document.getElementById('select').style.border = '';
});

class ColorPicker {
  constructor(colors) {
    this.colors = colors;
    this.index = 0;
  }

  getNextColor() {
    const color = this.colors[this.index];
    this.index = (this.index + 1) % this.colors.length;
    return color;
  }
}

function displayTokens(tokens) {
    const tokensContainer = document.getElementById('tokens');
    const colorPicker = new ColorPicker(colors);
    tokensContainer.innerHTML = '';
    tokens.forEach(token => {
        // If token is null or empty, skip it
        if (!token) {
            return;
        }
        const tokenSpan = document.createElement('span');
        tokenSpan.className = 'tokenizer-tkn';
        tokenSpan.innerText = token+' ';
        tokenSpan.style.backgroundColor = colorPicker.getNextColor();
        tokensContainer.appendChild(tokenSpan);

    });
}

function tokenize() {
    const inputText = document.getElementById('inputText').value;
    const modelName = document.getElementById('modelSelection').value;
    if (!inputText) {
        document.getElementById('inputText').style.borderColor = 'red';
        return;
    }
    if (!modelName) {
        document.getElementById('select').style.border = '1px solid red';
        document.getElementById('select').style.borderRadius = '.25rem';
        return;
    }
    const tokensContainer = document.getElementById('tokens');
    tokensContainer.innerHTML = '';
    fetch(apiUrl + 'tokenizer/tokenize', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            text: inputText,
            model_name: modelName
        })
    }).then(response => {
        if (!response.ok) {
            throw new Error('Failed to fetch tokens');
        }
        return response.json();
    }).then(data => {
        const tokens = data.tokens;
        document.getElementById('tokensCount').innerText = data.num_tokens;
        document.getElementById('charCount').innerText = data.num_chars;
        displayTokens(tokens);
    });
}

function clearText() {
    document.getElementById('inputText').value = '';
    document.getElementById('tokens').innerHTML = '';
    document.getElementById('tokensCount').innerText = '0';
    document.getElementById('charCount').innerText = '0';
}


const control = new TomSelect("#modelSelection", {
  plugins: [],
  create: true,
  render: {
    option: function(data, escape) {
      return '<div class="d-flex"><span> &nbsp; ' + escape(data.value) + '</span></div>';
    },
    item: function(data, escape) {
      return '<div>' + escape(data.value) + '</div>';
    }
  }
});

fetch(apiUrl + 'tokenizer/').then( response => {
    if (!response.ok) {
        throw new Error('Failed to fetch models');
    }
    return response.json()
}).then(data => {
    const modelSelection = document.getElementById('modelSelection');
    data.data.forEach(model => {
        control.addOption({value:model, text:model});
    });
});