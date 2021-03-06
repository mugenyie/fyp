let supervisor_list = "";
let count = 0;
function displaySupervisors(){
    GetData(baseurl+'supervisor/')
    .then(data => {
        console.log(JSON.stringify(data));
        data.forEach(element => {
            count+=1;
            supervisor_list += `
            <tr>
            <td>${element.name}</td>
            <td>${element.title}</td>
            <td>${element.department}</td>
            <td>${element.email}</td>
            <td>${element.phonenumber}</td>
            <td>${element.created_on}</td>
            </tr>
            `;
        });
        
        document.getElementById('supervisor-list').innerHTML = supervisor_list;
        document.getElementById('count').textContent = count;
    })
    .catch(error => console.error(error));  
}

let assigned_list = "";
let group_count_assigned = 0;
function displayAssignedGroups(){
    GetData(baseurl+`groups/${getCookie('id')}/assigned`)
    .then(data => {
        console.log(JSON.stringify(data));
        data.forEach(element => {
            group_count_assigned+=1;
            assigned_list += `
            <tr onclick="window.location.href='view_group?group_id=${element.id}'">
            <td>${element.name}</td>
            <td>${element.number}</td>
            <td>${element.project_name}</td>
            <td>${element.supervisor_name}</td>
            <td>${element.created_on}</td>
            </tr>
            `;
        });
        
        document.getElementById('group-list').innerHTML = assigned_list;
        document.getElementById('group-count').textContent = group_count_assigned;
    })
    .catch(error => console.error(error));  
}

function GetGroupProject(group_id){
    GetData(baseurl+`project/${group_id}/project`)
    .then(data => {
        console.log(JSON.stringify(data));
        document.getElementById('r-project_name').value = data.name;
        document.getElementById('project_id').value = data.id;
        document.getElementById('r-git_url').value = data.git_url;
        document.getElementById('r-web_url').value = data.web_url;
        document.getElementById('r-proposal_file').value = data.proposal_file;
        document.getElementById('r-documentation_file').value = data.documentation_file;
        document.getElementById('r-description').value = data.description;
        document.getElementById('r-score').value = data.score;
    })
    .catch(error => console.error(error));
}

function ScoreProject(){
    event.preventDefault();
    var project_id = document.getElementById('project_id').value;
    var score = document.getElementById('r-score').value;

    UpdateData(baseurl+`project/${project_id}`, {score:score})
    .then(data => {
        if(data.error){
            alert(data.error);
        }
        alert("Succesfuly Added Score");
    })
    .catch(error => console.error(error));  
}
/* <th>Title</th>
<th>Description</th>
<th>StudentId</th>
<th>Score</th>
<th>Created On</th> */
var group_log = "";
function GetGroupLog(group_id){
    GetData(baseurl+`projectlog/${group_id}/group`)
    .then(data => {
        console.log(JSON.stringify(data));
        data.forEach(element => {
            group_count_assigned+=1;
            group_log += `
            <tr onclick="window.location.href='score_log?log_id=${element.id}'">
            <td>${element.title}</td>
            <td>${element.description}</td>
            <td>${element.project_id}</td>
            <td>${element.supervisor_remarks}</td>
            <td>${element.score}</td>
            <td>${element.created_on}</td>
            </tr>
            `;
        });
        document.getElementById('group_log').innerHTML = group_log;
    })
    .catch(error => console.error(error));
}

function GetLogInfo(log_id){
    GetData(baseurl+`projectlog/${log_id}`)
    .then(data => {
        console.log(JSON.stringify(data));
        document.getElementById('r-title').value = data.title;
        document.getElementById('r-description').value = data.description;
        document.getElementById('r-files').value = data.files;
        document.getElementById('r-source').value = data.source_link;
        document.getElementById('r-score').value = data.score;
        document.getElementById('r-supervisor_remarks').value = data.supervisor_remarks;
    })
    .catch(error => console.error(error));
}

function ScoreLog(log_id){
    event.preventDefault();

    let score = document.getElementById('r-score').value;
    let remark = document.getElementById('r-supervisor_remarks').value;

    UpdateData(baseurl+`projectlog/${log_id}`,{score:score,supervisor_remarks:remark})
    .then(data => {
        if(data.error){
            alert(data.error);
        }else{
            alert("Successfuly awarded Project Log")
        }
        console.log(data);
    })
}

