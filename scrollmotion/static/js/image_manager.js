class ImageManagerApp extends React.Component {
	constructor(props){
		super(props);
		this.state = {
			images: [],
			selectImageIndex: null,
			imageData: null,
		}

		this.fetchImages = this.fetchImages.bind(this);
		this.selectUploadImage = this.selectUploadImage.bind(this);
		this.uploadImage = this.uploadImage.bind(this);
		this.showImageDetails = this.showImageDetails.bind(this);
		this.selectOriginal = this.selectOriginal.bind(this);
		this.selectCompressedOne = this.selectCompressedOne.bind(this);
		this.selectCompressedTwo = this.selectCompressedTwo.bind(this);

		// Fetch User Images
		this.fetchImages();
	}

	fetchImages(){
		console.log('Fetch Images');
		let _this = this;
		$.get('/image/', function(images){
			console.log(images);
			_this.setState({images: images});
		}, 'json')
	}

	selectUploadImage(event){
        event.stopPropagation();
        this.uploadInput.click();
    }

	uploadImage(){
		let _this = this;
        let data = new FormData();
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
                _this.fetchImages();
            }
        }, 'json');
	}

	showImageDetails(index){
		console.log('Show image details: ', index);
		this.setState({
						selectImageIndex: index,
						imageData: this.state.images[index]
						});
		$("#detailsModal").modal('show');
	}

	selectOriginal(){
		console.log('Select Original');
		let index = this.state.selectImageIndex;
		let imageData = this.state.images[index];
		this.setState({imageData: imageData});
	}

	selectCompressedOne(){
		console.log('Select Compressed One');
		let index = this.state.selectImageIndex;
		let imageData = this.state.images[index].compressed_one;
		this.setState({imageData: imageData});
	}

	selectCompressedTwo(){
		console.log('Select Compressed Two');
		let index = this.state.selectImageIndex;
		let imageData = this.state.images[index].compressed_two;
		this.setState({imageData: imageData});
	}

    render(){
        let _this = this;
        let images = this.state.images.map(function(image, index){
            return (
	            <div className="col-md-2 image-item-wrap" onClick={()=>_this.showImageDetails(index)}>
                    <div className="image-item">
                        <img src={squareImage} style={{background: 'url('+image.url+') center center', backgroundSize: 'cover'}}/>
                    </div>
                </div>
            );
        });

        let image = this.state.imageData;
        let imageDetails = null;
        if(image){
            imageDetails = (
                                <div className="main-section">
                                    <img src={image.url}/>
                                    <div className="attribute-group">
                                        <div className="attribute">
                                            <div className="name">Size: </div>
                                            <div className="value">{Math.round(image.size/1000)}kb</div>
                                        </div>
                                        <div className="attribute">
                                            <div className="name">Type: </div>
                                            <div className="value">JPEG</div>
                                        </div>
                                        <div className="attribute">
                                            <div className="name">Quality: </div>
                                            <div className="value">{image.quality}</div>
                                        </div>
                                    </div>
                                    <a className="btn btn-info" href={image.url} download>Download</a>
                                </div>
            );
        }
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
                                    <div className="img-btn" onClick={this.selectOriginal}>Original</div>
                                    <div className="img-btn" onClick={this.selectCompressedOne}>Compressed 1</div>
                                    <div className="img-btn" onClick={this.selectCompressedTwo}>Compressed 2</div>
                                </div>
                                {imageDetails}
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