# Multiview_ByteTrack

I extend ByteTrack from single-view to multi-view with centroids-reid as the association method between different views.

# Note

1. Only two views are supported for this code.
2. Create a new folder named ***MultiView_ByteTrack/videos*** and put your videos in it
3. Download the pretrained weights from github website of ByteTrack(put it in a new folder named ***MultiView_ByteTrack/pretrained/***) and CTL(put it in a new folder named ***MultiView_ByteTrack/encoder_weights/***)
4. For CTL, I used r50-ibn. For r50, network and image input size should be changed.
5. Command line input is in command.txt (remember to change the camid)
   
# Reference:

@article{Wieczorek2021OnTU,
  title={On the Unreasonable Effectiveness of Centroids in Image Retrieval},
  author={Mikolaj Wieczorek and Barbara Rychalska and Jacek Dabrowski},
  journal={ArXiv},
  year={2021},
  volume={abs/2104.13643}
}

@article{zhang2022bytetrack,
  title={ByteTrack: Multi-Object Tracking by Associating Every Detection Box},
  author={Zhang, Yifu and Sun, Peize and Jiang, Yi and Yu, Dongdong and Weng, Fucheng and Yuan, Zehuan and Luo, Ping and Liu, Wenyu and Wang, Xinggang},
  booktitle={Proceedings of the European Conference on Computer Vision (ECCV)},
  year={2022}
}

