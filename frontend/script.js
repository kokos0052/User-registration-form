const nameInput = document.getElementById("input1");
const surnameInput = document.getElementById("input2");
const thirdnameInput = document.getElementById("input3");
const phoneInput = document.getElementById("input4");
const reviewInput = document.getElementById("input5");

const sendButton = document.getElementById("send-button");

async function sendData(url, data, config) {
  const domain = "http://127.0.0.1:5080";

  const request = await fetch(`${domain}/${url}`, {
    ...config,
    method: "POST",
    body: JSON.stringify(data),
  });

  return await request.json();
}

sendButton.addEventListener("click", (e) => {
  e.preventDefault();

  const data = {
    name: nameInput.value,
    surname: surnameInput.value,
    thirdname: thirdnameInput.value,
    phone: phoneInput.value,
    review: reviewInput.value,
  };

  sendData("send", data);
});
