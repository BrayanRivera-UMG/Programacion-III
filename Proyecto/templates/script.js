
// Collapsibles
document.querySelectorAll('.collapsible').forEach(btn=>{
  btn.addEventListener('click',function(){
    this.classList.toggle('active');
    const c=this.nextElementSibling;
    c.style.maxHeight = c.style.maxHeight ? null : c.scrollHeight+'px';
  });
});

// Leaflet setup
const map = L.map('map').setView([15.5,-90.25],7);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{maxZoom:19}).addTo(map);

let markers=[],routingControls=[],lastRecommendations=[],entitiesMap={};

function clearMap(){
  markers.forEach(m=>map.removeLayer(m));
  routingControls.forEach(rc=>map.removeControl(rc));
  markers=[];routingControls=[];
}

function showRecommendations(data){
  clearMap();
  lastRecommendations=data;
  const cont=document.getElementById('recommendations');
  cont.innerHTML='';
  if(!data.length){ cont.innerHTML='<p>No se encontraron recomendaciones.</p>'; return; }
  const originId=data[0].origin;
  const originEnt=entitiesMap[originId];
  const origM=L.marker([originEnt.latitude,originEnt.longitude]).addTo(map)
    .bindPopup('<b>Origen:</b> '+originEnt.name);
  markers.push(origM);
  let lastPoint=L.latLng(originEnt.latitude,originEnt.longitude);
  let html='<h2>Recomendaciones</h2>';
  data.forEach(rec=>{
    const ent=rec.entity;
    html+=`<div class="recommendation-item"><h3>${ent.name}</h3>
      <p><b>ID:</b>${ent.identifier} <b>Precio:</b>${ent.price}
      <b>Calif:</b>${ent.average_rating.toFixed(2)}
      <b>Estadía:</b>${ent.estimated_stay||0}h
      <b>Dist:</b>${rec.travel_distance.toFixed(1)}km
      <b>Viaje:</b>${Math.round(rec.travel_time*60)}min</p></div>`;
    const m=L.marker([ent.latitude,ent.longitude]).addTo(map).bindPopup(ent.name);
    markers.push(m);
    const dest=L.latLng(ent.latitude,ent.longitude);
    const rc=L.Routing.control({waypoints:[lastPoint,dest],
      routeWhileDragging:false,addWaypoints:false,draggableWaypoints:false,
      lineOptions:{styles:[{opacity:0.7,weight:5}]},show:false
    }).addTo(map);
    routingControls.push(rc);
    lastPoint=dest;
  });
  cont.innerHTML=html;
  map.fitBounds(L.featureGroup(markers).getBounds().pad(0.3));
}

// Nuevo buildGraphNetwork sin overlap
function buildGraphNetwork(data){
  const ids=[data[0].origin].concat(data.map(r=>r.entity.identifier));
  const lats=ids.map(id=>entitiesMap[id].latitude),
        lons=ids.map(id=>entitiesMap[id].longitude);
  const minLat=Math.min(...lats),maxLat=Math.max(...lats),
        minLon=Math.min(...lons),maxLon=Math.max(...lons);
  const container=document.getElementById('network'),
        W=container.clientWidth,H=container.clientHeight,
        pad=50;
  const nodes=ids.map(id=>{
    const ent=entitiesMap[id];
    const nx=(ent.longitude-minLon)/(maxLon-minLon),
          ny=1-(ent.latitude-minLat)/(maxLat-minLat);
    const x=pad+nx*(W-2*pad)-W/2, y=pad+ny*(H-2*pad)-H/2;
    return {
      id,label:id===data[0].origin?'Origen\\n'+ent.name:ent.name,
      x,y,fixed:{x:true,y:true},
      shape:'dot',size:18,font:{size:14},
      color:id===data[0].origin?'#ff6666':undefined
    };
  });
  const edges=[];
  for(let i=0;i<ids.length;i++){
    for(let j=i+1;j<ids.length;j++){
      const a=ids[i],b=ids[j];
      const p1=L.latLng(entitiesMap[a].latitude,entitiesMap[a].longitude),
            p2=L.latLng(entitiesMap[b].latitude,entitiesMap[b].longitude);
      const d=(p1.distanceTo(p2)/1000).toFixed(1);
      edges.push({
        from:a,to:b,label:d+' km',
        font:{size:12,align:'top'},
        smooth:{type:'curvedCW',roundness:0.2}
      });
    }
  }
  const dataVis={nodes:new vis.DataSet(nodes),edges:new vis.DataSet(edges)};
  new vis.Network(container,dataVis,{
    physics:false,layout:{improvedLayout:false},interaction:{hover:true}
  });
}

document.getElementById('show-graph-btn').addEventListener('click',()=>{
  const nc=document.getElementById('network-container');
  nc.style.maxHeight=nc.style.maxHeight?null:nc.scrollHeight+'px';
  if(lastRecommendations.length) buildGraphNetwork(lastRecommendations);
});

async function loadDataTable(){
  const res=await fetch('/get_entities'), js=await res.json();
  entitiesMap=Object.fromEntries(js.entities.map(e=>[e.identifier,e]));
  const tb=document.getElementById('data-table-body');
  tb.innerHTML='';
  js.entities.sort((a,b)=>+a.identifier-+b.identifier).forEach(e=>{
    const tr=document.createElement('tr');
    tr.innerHTML=`
      <td>${e.identifier}</td><td>${e.name}</td><td>${e.entity_type}</td>
      <td>${e.latitude}</td><td>${e.longitude}</td>
      <td>${e.price}</td><td>${e.average_rating.toFixed(2)}</td>
      <td>${e.estimated_stay||'N/A'}</td>`;
    tb.appendChild(tr);
  });
}

document.getElementById('upload-places').onsubmit=async e=>{
  e.preventDefault();
  const f=document.getElementById('file-places');
  if(!f.files.length) return alert('Seleccione CSV');
  const fd=new FormData(); fd.append('file',f.files[0]);
  const r=await fetch('/upload_entities',{method:'POST',body:fd});
  alert(await r.text()); if(r.ok) await loadDataTable();
};
document.getElementById('upload-ratings').onsubmit=async e=>{
  e.preventDefault();
  const f=document.getElementById('file-ratings');
  if(!f.files.length) return alert('Seleccione CSV');
  const fd=new FormData(); fd.append('file',f.files[0]);
  const r=await fetch('/upload_ratings',{method:'POST',body:fd});
  alert((await r.json()).message); await loadDataTable();
};
document.getElementById('recommend-form').onsubmit=async e=>{
  e.preventDefault();
  const origin=document.getElementById('origin').value.trim(),
        budget=parseFloat(document.getElementById('budget').value);
  if(!origin||isNaN(budget)||budget<=0) return alert('Datos inválidos');
  const r=await fetch('/recommend',{
    method:'POST',headers:{'Content-Type':'application/json'},
    body:JSON.stringify({origin,budget})
  });
  const js=await r.json();
  if(js.error) return alert(js.error);
  if(js.recommendations.length) js.recommendations[0].origin=origin;
  showRecommendations(js.recommendations);
};
document.getElementById('manual-form').onsubmit=async e=>{
  e.preventDefault();
  const data={}; new FormData(e.target).forEach((v,k)=>data[k]=v);
  const r=await fetch('/add_manual',{method:'POST',
    headers:{'Content-Type':'application/json'},body:JSON.stringify(data)});
  alert(await r.text()); if(r.ok){e.target.reset();await loadDataTable();}
};
document.getElementById('show-data-btn').addEventListener('click',loadDataTable);
