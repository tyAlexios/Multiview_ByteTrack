# Multiview_ByteTrack

I extend ByteTrack from single-view to multi-view with centroids-reid as the association method between different views.

# Demo


# Note

1. Follow the instructions in ByteTrack github page to set it up
2. Command line input is in command.txt (remember to change the camid)
3. Create a new folder named ***MultiView_ByteTrack/videos*** and put your videos in it
4. Download the pretrained weights from github website of ByteTrack(put it in a new folder named ***MultiView_ByteTrack/pretrained/***) and CTL(put it in a new folder named ***MultiView_ByteTrack/encoder_weights/***)
5. For CTL, I used r50-ibn. For r50, network and image input size should be changed.
6. Only two views are supported for this code.
   
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

