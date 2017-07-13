class ImageManagerApp extends React.Component {
	constructor(props){
		super(props);
		this.state = {
			images: []
		}

		this.fetchImages = this.fetchImages.bind(this);
		this.selectUploadImage = this.selectUploadImage.bind(this);
		this.uploadImage = this.uploadImage.bind(this);

		// Fetch User Images
		this.fetchImages();
	}

	fetchImages(){
		console.log('fetch images');
		let _this = this;
		$.get('/image/', function(images){
			console.log('user images returned');
			console.log(images);
			_this.setState({images: images});
		}, 'json')
	}

	selectUploadImage(event){
        event.stopPropagation();
        this.uploadInput.click();
    }

	uploadImage(){
        var data = new FormData();
        data.append('image', this.uploadInput.files[0]);
        $.ajax({
            url: '/image/',
            type: 'POST',
            data: data,
            processData: false,
            contentType: false,
            success: function(data, textStatus, jqXHR)
            {
                console.log(data);
            }
        }, 'json');
	}

    render(){
        let images = this.state.images.map(function(image){
            return (
	            <div className="col-md-2 image-item-wrap">
                    <div className="image-item" data-toggle="modal" data-target="#detailsModal">
                        <img src={squareImage} style={{background: 'url('+image.image_url+') center center', backgroundSize: 'cover'}}/>
                    </div>
                </div>
            );
        });
        return (
            <div>
                <div className="modal fade" id="detailsModal">
                    <div className="modal-dialog">
                        <div className="modal-content">
                            <div className="modal-header">
                                <button type="button" className="close" data-dismiss="modal"><span>&times;</span></button>
                                <h4 className="modal-title">Image Details</h4>
                            </div>
                            <div className="modal-body">
                                <div className="side-section">
                                    <div className="img-btn">Original</div>
                                    <div className="img-btn">Compressed 1</div>
                                    <div className="img-btn">Compressed 2</div>
                                </div>
                                <div className="main-section">
                                    <img src="https://s3.amazonaws.com/scrollmotion/original/elephant.jpg"/>
                                    <div className="attribute-group">
                                        <div className="attribute">
                                            <div className="name">Name</div>
                                            <div className="value">something.jpg</div>
                                        </div>
                                        <div className="attribute">
                                            <div className="name">Size</div>
                                            <div className="value">13kb</div>
                                        </div>
                                        <div className="attribute">
                                            <div className="name">Type</div>
                                            <div className="value">JPEG</div>
                                        </div>
                                        <div className="attribute">
                                            <div className="name">Quality</div>
                                            <div className="value">80</div>
                                        </div>
                                    </div>
                                    <button className="btn btn-info">Download</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div className="container-fluid">

                    <div className="header">
                        <div className="brand">
                            <img className='logo' src={logoImage}/>
                            <span>Image Manager</span>
                        </div>

                        <div id="image-uploader" className="control-group">
                            <button id="upload-btn" type="button" className="btn btn-info" onClick={this.selectUploadImage} >Upload</button>
                            <a href="{% url 'logout' %}" className="btn btn-info">Logout</a>
                        </div>
                    </div>

                    <div className="row">
                        {images}
                    </div>

                    <input id="newImageInput" type="file" style={{display: 'none'}} ref={(input) => { this.uploadInput = input; }} onChange={(e)=>this.uploadImage()}/>
                </div>
            </div>
        );
    }
}
ReactDOM.render(<ImageManagerApp/>, document.getElementById('image-manager-container') );