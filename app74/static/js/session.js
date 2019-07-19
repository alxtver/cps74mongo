function addSession() {
    let field_name_type = document.getElementById("id_name_type").value;
    let field_part_name = document.getElementById("id_part_name").value;
    let field_name = document.getElementById("id_name").value;
    let field_country = document.getElementById("id_country").value;
    sessionStorage.setItem("id_name_type", field_name_type);
    sessionStorage.setItem("id_part_name", field_part_name);
    sessionStorage.setItem("id_name", field_name);
    sessionStorage.setItem("id_country", field_country);
}
function insSession() {
    let field_name_type = document.getElementById("id_name_type");
    let field_part_name = document.getElementById("id_part_name");
    let field_name = document.getElementById("id_name");
    let field_country = document.getElementById("id_country");
    if (sessionStorage.getItem("id_name_type")) {
        field_name_type.value = sessionStorage.getItem("id_name_type")
    }
    if (sessionStorage.getItem("id_part_name")) {
        field_part_name.value = sessionStorage.getItem("id_part_name")
    }
    if (sessionStorage.getItem("id_name")) {
        field_name.value = sessionStorage.getItem("id_name")
    }
    if (sessionStorage.getItem("id_country")) {
        field_country.value = sessionStorage.getItem("id_country")
    }

}
function loadSession() {
  let field_name_type = document.getElementById("id_name_type");
  let field_part_name = document.getElementById("id_part_name");
  let field_name = document.getElementById("id_name");
  let field_country = document.getElementById("id_country");
  if (sessionStorage.getItem("id_name_type")) {
      field_name_type.value = sessionStorage.getItem("id_name_type")
  }
  if (sessionStorage.getItem("id_part_name")) {
      field_part_name.value = sessionStorage.getItem("id_part_name")
  }
  if (sessionStorage.getItem("id_name")) {
      field_name.value = sessionStorage.getItem("id_name")
  }
  if (sessionStorage.getItem("id_country")) {
      field_country.value = sessionStorage.getItem("id_country")
  }
  document.getElementById("id_serial_number").focus();
}
