const projectLocationSearch = async (event) => {
  const projectLocationNode = document.getElementById('project-location');
  const value = await askForFolder();
  if (value != null) {
    projectLocationNode.value = value;
  }
}

const generateVerilog = async (event) => {
  const projectLocation = document.getElementById('project-location').value;
  if (!projectLocation) {
    alert('Please provide project location');
    return;
  }

  const N = document.getElementById('n-bits').value;
  if (!N) {
    alert('Please provide the size of the adder');
    return;
  }

  eel.generateVerilog(projectLocation, currentAdder, Number.parseInt(N));
}

const setupEvents = () => {
  document.getElementById('project-location-search').addEventListener('click', projectLocationSearch);
  document.getElementById('generate-button').addEventListener('click', generateVerilog);
}