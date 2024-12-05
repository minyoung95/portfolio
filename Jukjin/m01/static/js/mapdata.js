var simplemaps_countrymap_mapdata={
  main_settings: {
   //General settings
    width: "900", //'700' or 'responsive'
    height: "770", //'700' or 'responsive'
    background_color: "#FFFFFF",
    background_transparent: "yes",
    border_color: "#ffffff",
    
    //State defaults
    state_description: "",
    state_color: "#bfde9c",
    state_hover_color: "#ed6b6b",
    state_url: "",
    border_size: "3",
    all_states_inactive: "no",
    all_states_zoomable: "no",
    
    //Location defaults
    location_description: "Location description",
    location_url: "",
    location_color: "#bfde9c",
    location_opacity: 0.8,
    location_hover_opacity: 1,
    location_size: 25,
    location_type: "square",
    location_image_source: "frog.png",
    location_border_color: "#FFFFFF",
    location_border: 2,
    location_hover_border: 2.5,
    all_locations_inactive: "no",
    all_locations_hidden: "no",
    
    //Label defaults
    label_color: "#ffffff",
    label_hover_color: "#ffffff",
    label_size: 16,
    label_font: "Arial",
    label_display: "auto",
    label_scale: "yes",
    hide_labels: "no",
    hide_eastern_labels: "no",
   
    // //Zoom settings
    // zoom: "yes",
    // manual_zoom: "yes",
    // back_image: "no",
    // initial_back: "no",
    // initial_zoom: "-1",
    // initial_zoom_solo: "no",
    // region_opacity: 1,
    // region_hover_opacity: 0.6,
    // zoom_out_incrementally: "yes",
    // zoom_percentage: 0.99,
    // zoom_time: 0.5,
    
    //Popup settings
    popup_color: "white",
    popup_opacity: 0.9,
    popup_shadow: 1,
    popup_corners: 5,
    popup_font: "12px/1.5 Verdana, Arial, Helvetica, sans-serif",
    popup_nocss: "no",
    
    //Advanced settings
    div: "map",
    auto_load: "yes",
    url_new_tab: "no",
    images_directory: "default",
    fade_time: 0.1,
    link_text: "View Website",
    popups: "detect",
    state_image_url: "",
    state_image_position: "",
    location_image_url: ""
  },
  state_specific: {
    KR11: {
      name: "서울",
      state_hover_color: "blue",
    },
    KR26: {
      name: "부산"
    },
    KR27: {
      name: "대구"
    },
    KR28: {
      name: "인천"
    },
    KR29: {
      name: "광주"
    },
    KR30: {
      name: "대전"
    },
    KR31: {
      name: "울산"
    },
    KR41: {
      name: "경기도"
    },
    KR42: {
      name: "강원도"
    },
    KR43: {
      name: "충청북도"
    },
    KR44: {
      name: "충청남도"
    },
    KR45: {
      name: "전라북도"
    },
    KR46: {
      name: "전라남도"
    },
    KR47: {
      name: "경상북도"
    },
    KR48: {
      name: "경상남도"
    },
    KR49: {
      name: "제주도"
    }
  },
  locations: {
    "1": {
      lat: "37.48057500",
      lng: "130.9037889",
      name: "울룽도,독도",
      size: "30"
    }
  },
  labels: {
    KR11: {
      name: "서울",
      parent_id: "KR11"
    },
    KR26: {
      name: "부산",
      parent_id: "KR26"
    },
    KR27: {
      name: "대구",
      parent_id: "KR27"
    },
    KR28: {
      parent_id: "KR28",
      name: "인천"
    },
    KR29: {
      name: "광주",
      parent_id: "KR29"
    },
    KR30: {
      name: "대전",
      parent_id: "KR30"
    },
    KR31: {
      name: "울산",
      parent_id: "KR31"
    },
    KR41: {
      parent_id: "KR41",
      name: "경기도"
    },
    KR42: {
      parent_id: "KR42",
      name: "강원도"
    },
    KR43: {
      parent_id: "KR43",
      name: "충청북도"
    },
    KR44: {
      parent_id: "KR44",
      name: "충청남도"
    },
    KR45: {
      parent_id: "KR45",
      name: "전라북도"
    },
    KR46: {
      parent_id: "KR46",
      name: "전라남도"
    },
    KR47: {
      parent_id: "KR47",
      name: "경상북도"
    },
    KR48: {
      parent_id: "KR48",
      name: "경상남도"
    },
    KR49: {
      parent_id: "KR49",
      name: "제주도"
    }
  },
  state_click: function(parent_id) {
    if (parent_id === "KR11") {
      alert("서울이 클릭되었습니다!");
    } else {
      alert(state_id + " 지역이 클릭되었습니다.");
    }
  },
  legend: {
    entries: []
  },
  regions: {}
  
};
