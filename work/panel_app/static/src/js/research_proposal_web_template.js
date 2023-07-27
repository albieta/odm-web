if (document.getElementById('proposals-container')) {
  let proposals = document.querySelectorAll('.resources');
  let keywords = [];
  const universityButtons = document.querySelectorAll('.university-btn');

  let selectedUniversity = null;
  let selectedKeywords = [];
  let searchQuery = "";
  let page = 1; 

  function requestInfrastructures() {
    let data = {
      'page': page,
    };

    if (searchQuery !== '') {
      data['search_query'] = searchQuery;
    }
    if (selectedKeywords.length > 0) {
      data['keywords'] = selectedKeywords.join(',');
    }
    if (selectedUniversity) {
      data['university'] = selectedUniversity;
    }

    $.ajax({
      type: "POST",
      url: "/research/proposal/filtered",
      data: data,
      success: function(data) {

        $('#proposals-container').html(data);
        updateFunctions();
      },
      error: function(xhr, textStatus, errorThrown) {
          console.log(textStatus + ': ' + errorThrown);
      }
    });
  }

  function updateFunctions() {
    proposals = document.querySelectorAll('.resources');

    proposals.forEach((resource) => {
      const cardTitle = resource.querySelector('.card-title-toggle');
      const cardBody = resource.querySelector('.card-body');
      cardBody.classList.toggle('d-none');
    
      cardTitle.addEventListener('click', () => {
        cardBody.classList.toggle('d-none');
      });
    });
    
    $('.left-btn').click(function() {
      if (page > 1) {
        page = page - 1;
        requestInfrastructures();
      }
    });

    $('.right-btn').click(function() {
      if (page < document.querySelector('.products_pager').dataset.max) {
        page = page + 1;
        requestInfrastructures();
      }
    });
  }

  $(document).ready(function() {

    universityButtons.forEach(button => {
      button.addEventListener('click', () => {
        if (button.classList.contains('selected')) {
          button.classList.remove('selected');
          selectedUniversity = null;
        } else {
          universityButtons.forEach(btn => btn.classList.remove('selected'));
          button.classList.add('selected');
          selectedUniversity = button.dataset.university;
        }
        page = 1;
        requestInfrastructures();
      });
    });

    requestInfrastructures();
  });

  $(document).ready(function () {
    $.ajax({
      type: "GET",
      url: "/research/proposal/keywords",
      success: function(data) {
        keywords = data.keywords;
        $('#keywords').selectivity({
          items: keywords,
          multiple: true,
          placeholder: "   Filter by tags..."
        });
        document.querySelector('.tags-list').addEventListener('selectivity-change',function(event) {
          if(event.added){
            selectedKeywords.push(event.value);
          } else {
            selectedKeywords = event.value.filter((value) => typeof value === 'string');
          }
          page = 1;
          requestInfrastructures();
        });
      },
      error: function(xhr, textStatus, errorThrown) {
          console.log(textStatus + ': ' + errorThrown);
      }
    })
  });

  function handleSearchForm() {
    page = 1;
    event.preventDefault();
    searchQuery = document.getElementById('search-query').value;
    requestInfrastructures();
  }

}