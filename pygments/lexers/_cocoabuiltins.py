# -*- coding: utf-8 -*-
"""
    pygments.lexers._cocoabuiltins
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This file defines a set of types used across Cocoa frameworks from Apple.
    There is a list of @interfaces, @protocols and some other (structs, unions)

    File may be also used as standalone generator for aboves.

    :copyright: Copyright 2006-2014 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""
from __future__ import print_function

COCOA_INTERFACES = set(['UITableViewCell', 'NSURLSessionDataTask', 'NSLinguisticTagger', 'NSStream', 'UIPrintInfo', 'SKPaymentTransaction', 'SKPhysicsWorld', 'NSString', 'CMAttitude', 'SKSpriteNode', 'JSContext', 'UICollectionReusableView', 'AVMutableCompositionTrack', 'GKLeaderboard', 'NSFetchedResultsController', 'MKTileOverlayRenderer', 'MIDINetworkSession', 'UITextSelectionRect', 'MKRoute', 'MPVolumeView', 'UIKeyCommand', 'AVMutableAudioMix', 'GLKEffectPropertyLight', 'UICollectionViewLayout', 'NSMutableCharacterSet', 'UIAccessibilityElement', 'NSShadow', 'NSAtomicStoreCacheNode', 'UIPushBehavior', 'CBCharacteristic', 'CBUUID', 'CMStepCounter', 'NSNetService', 'UICollectionView', 'UIViewPrintFormatter', 'CAShapeLayer', 'MCPeerID', 'NSFileVersion', 'CMGyroData', 'SKPhysicsJointSpring', 'CIFilter', 'UIView', 'MKMapItem', 'PKPass', 'MKPolygonRenderer', 'JSValue', 'CLGeocoder', 'NSByteCountFormatter', 'AVCaptureScreenInput', 'CAAnimation', 'MKOverlayPathView', 'UIActionSheet', 'UIMotionEffectGroup', 'UIBarItem', 'SKProduct', 'AVAssetExportSession', 'NSKeyedUnarchiver', 'NSMutableSet', 'MKMapView', 'CATransition', 'CLCircularRegion', 'MKTileOverlay', 'UICollisionBehavior', 'ACAccountCredential', 'SKPhysicsJointLimit', 'AVMediaSelectionGroup', 'NSIndexSet', 'AVAudioRecorder', 'NSURL', 'CBCentral', 'NSNumber', 'UITableView', 'AVCaptureStillImageOutput', 'GCController', 'NSAssertionHandler', 'AVAudioSessionPortDescription', 'NSHTTPURLResponse', 'NSPropertyListSerialization', 'AVPlayerItemAccessLogEvent', 'UISwipeGestureRecognizer', 'MKOverlayRenderer', 'NSDecimalNumber', 'EKReminder', 'MKPolylineView', 'AVCaptureMovieFileOutput', 'UIImagePickerController', 'GKAchievementDescription', 'EKParticipant', 'NSBlockOperation', 'UIActivityItemProvider', 'CLLocation', 'GKLeaderboardViewController', 'MPMoviePlayerController', 'GKScore', 'NSURLConnection', 'ABUnknownPersonViewController', 'UIMenuController', 'NSEvent', 'SKTextureAtlas', 'NSKeyedArchiver', 'GKLeaderboardSet', 'NSSimpleCString', 'CBATTRequest', 'GKMatchRequest', 'AVMetadataObject', 'UIAlertView', 'NSIncrementalStore', 'MFMailComposeViewController', 'SSReadingList', 'MPMovieAccessLog', 'NSManagedObjectContext', 'AVCaptureAudioDataOutput', 'ACAccount', 'AVMetadataItem', 'AVCaptureDeviceInputSource', 'CLLocationManager', 'UIStepper', 'UIRefreshControl', 'GKTurnBasedParticipant', 'UICollectionViewTransitionLayout', 'CBCentralManager', 'NSPurgeableData', 'SLComposeViewController', 'NSHashTable', 'MKUserTrackingBarButtonItem', 'UITabBarController', 'CMMotionActivity', 'SKAction', 'AVPlayerItemOutput', 'UIDocumentInteractionController', 'UIDynamicItemBehavior', 'NSMutableDictionary', 'UILabel', 'AVCaptureInputPort', 'NSExpression', 'SKMutablePayment', 'UIStoryboardSegue', 'NSOrderedSet', 'UIPopoverBackgroundView', 'UIToolbar', 'NSNotificationCenter', 'NSEntityMigrationPolicy', 'NSLocale', 'NSURLSession', 'NSTimeZone', 'UIManagedDocument', 'AVMutableVideoCompositionLayerInstruction', 'AVAssetTrackGroup', 'NSInvocationOperation', 'ALAssetRepresentation', 'AVQueuePlayer', 'UIPasteboard', 'NSLayoutManager', 'EKCalendarChooser', 'EKObject', 'CATiledLayer', 'GLKReflectionMapEffect', 'NSManagedObjectID', 'NSUserDefaults', 'SLRequest', 'AVPlayerLayer', 'NSPointerArray', 'AVAudioMix', 'MCAdvertiserAssistant', 'MKMapSnapshotOptions', 'GKMatch', 'AVTimedMetadataGroup', 'CBMutableCharacteristic', 'NSFetchRequest', 'UIDevice', 'NSManagedObject', 'NKAssetDownload', 'AVOutputSettingsAssistant', 'SKPhysicsJointPin', 'UITabBar', 'UITextInputMode', 'NSFetchRequestExpression', 'NSPipe', 'AVComposition', 'ADBannerView', 'AVPlayerItem', 'AVSynchronizedLayer', 'MKDirectionsRequest', 'NSMetadataItem', 'UINavigationItem', 'CBPeripheralManager', 'UIStoryboardPopoverSegue', 'SKProductsRequest', 'UIGravityBehavior', 'UIWindow', 'CBMutableDescriptor', 'UIBezierPath', 'UINavigationController', 'ABPeoplePickerNavigationController', 'EKSource', 'AVAssetWriterInput', 'AVPlayerItemTrack', 'GLKEffectPropertyTexture', 'NSURLResponse', 'SKPaymentQueue', 'MKReverseGeocoder', 'GCControllerAxisInput', 'MKMapSnapshotter', 'NSOrthography', 'NSURLSessionUploadTask', 'NSCharacterSet', 'AVAssetReaderOutput', 'EAGLContext', 'UICollectionViewController', 'AVAssetTrack', 'SKEmitterNode', 'AVCaptureDeviceInput', 'AVVideoCompositionCoreAnimationTool', 'NSURLRequest', 'CMAccelerometerData', 'NSNetServiceBrowser', 'AVAsynchronousVideoCompositionRequest', 'CAGradientLayer', 'NSFormatter', 'CATransaction', 'MPMovieAccessLogEvent', 'UIStoryboard', 'MPMediaLibrary', 'UITapGestureRecognizer', 'MPMediaItemArtwork', 'NSURLSessionTask', 'MCBrowserViewController', 'NSRelationshipDescription', 'NSMutableAttributedString', 'MPNowPlayingInfoCenter', 'MKLocalSearch', 'EAAccessory', 'MKETAResponse', 'CATextLayer', 'NSNotificationQueue', 'NSValue', 'NSMutableIndexSet', 'SKPhysicsContact', 'NSProgress', 'CAScrollLayer', 'NSTextCheckingResult', 'NSEntityDescription', 'NSURLCredentialStorage', 'UIApplication', 'SKDownload', 'MKLocalSearchRequest', 'SKScene', 'UISearchDisplayController', 'CAReplicatorLayer', 'UIPrintPageRenderer', 'EKCalendarItem', 'NSUUID', 'EAAccessoryManager', 'AVAssetResourceLoader', 'AVMutableVideoCompositionInstruction', 'MyClass', 'CTCall', 'CIVector', 'UINavigationBar', 'UIPanGestureRecognizer', 'MPMediaQuery', 'ABNewPersonViewController', 'ACAccountType', 'GKSession', 'SKVideoNode', 'GCExtendedGamepadSnapshot', 'GCExtendedGamepad', 'CAValueFunction', 'UIActivityIndicatorView', 'NSNotification', 'SKReceiptRefreshRequest', 'AVCaptureDeviceFormat', 'AVPlayerItemErrorLog', 'NSMapTable', 'NSSet', 'CMMotionManager', 'GKVoiceChatService', 'UIPageControl', 'MKGeodesicPolyline', 'AVMutableComposition', 'NSLayoutConstraint', 'UIWebView', 'NSIncrementalStoreNode', 'EKEventStore', 'UISlider', 'AVAssetResourceLoadingRequest', 'AVCaptureInput', 'SKPhysicsBody', 'NSOperation', 'MKMapCamera', 'SKProductsResponse', 'GLKEffectPropertyMaterial', 'AVCaptureDevice', 'CTCallCenter', 'CBMutableService', 'SKTransition', 'UIDynamicAnimator', 'NSMutableArray', 'MCNearbyServiceBrowser', 'NSOperationQueue', 'MKPolylineRenderer', 'UICollectionViewLayoutAttributes', 'NSValueTransformer', 'UICollectionViewFlowLayout', 'NSEntityMapping', 'SKTexture', 'NSMergePolicy', 'UITextInputStringTokenizer', 'NSRecursiveLock', 'AVAsset', 'NSUndoManager', 'MPMediaPickerController', 'NSFileCoordinator', 'NSFileHandle', 'NSConditionLock', 'UISegmentedControl', 'NSManagedObjectModel', 'UITabBarItem', 'MPMediaItem', 'EKRecurrenceRule', 'UIEvent', 'UITouch', 'UIPrintInteractionController', 'CMDeviceMotion', 'NSCompoundPredicate', 'MKMultiPoint', 'UIPrintFormatter', 'SKView', 'NSConstantString', 'UIPopoverController', 'AVMetadataFaceObject', 'EKEventViewController', 'NSPort', 'MKCircleRenderer', 'AVCompositionTrack', 'UINib', 'NSUbiquitousKeyValueStore', 'NSMetadataQueryResultGroup', 'AVAssetResourceLoadingDataRequest', 'UITableViewHeaderFooterView', 'UISplitViewController', 'AVAudioSession', 'CAEmitterLayer', 'NSNull', 'MKCircleView', 'UIColor', 'UIAttachmentBehavior', 'CLBeacon', 'NSInputStream', 'NSURLCache', 'GKPlayer', 'NSMappingModel', 'NSHTTPCookie', 'AVMutableVideoComposition', 'NSAttributeDescription', 'AVPlayer', 'MKAnnotationView', 'UIFontDescriptor', 'NSTimer', 'CBDescriptor', 'MKOverlayView', 'EKEventEditViewController', 'NSSaveChangesRequest', 'UIReferenceLibraryViewController', 'SKPhysicsJointFixed', 'UILocalizedIndexedCollation', 'UIInterpolatingMotionEffect', 'AVAssetWriter', 'NSBundle', 'SKStoreProductViewController', 'GLKViewController', 'NSMetadataQueryAttributeValueTuple', 'GKTurnBasedMatch', 'UIActivity', 'MKShape', 'NSMergeConflict', 'CIImage', 'UIRotationGestureRecognizer', 'AVPlayerItemLegibleOutput', 'AVAssetImageGenerator', 'GCControllerButtonInput', 'NSSortDescriptor', 'MPTimedMetadata', 'NKIssue', 'UIScreenMode', 'GKTurnBasedEventHandler', 'MKPolyline', 'JSVirtualMachine', 'AVAssetReader', 'NSAttributedString', 'GKMatchmakerViewController', 'NSCountedSet', 'UIButton', 'GKLocalPlayer', 'MPMovieErrorLog', 'AVSpeechUtterance', 'AVURLAsset', 'CBPeripheral', 'AVAssetWriterInputGroup', 'AVAssetReaderAudioMixOutput', 'NSEnumerator', 'UIDocument', 'MKLocalSearchResponse', 'UISimpleTextPrintFormatter', 'CBService', 'MCSession', 'QLPreviewController', 'CAMediaTimingFunction', 'UITextPosition', 'NSNumberFormatter', 'UIPinchGestureRecognizer', 'UIMarkupTextPrintFormatter', 'MKRouteStep', 'NSMetadataQuery', 'AVAssetResourceLoadingContentInformationRequest', 'CTSubscriber', 'CTCarrier', 'NSFileSecurity', 'UIAcceleration', 'UIMotionEffect', 'CLHeading', 'NSFileWrapper', 'MKDirectionsResponse', 'UILocalNotification', 'UICollectionViewCell', 'UITextView', 'CMMagnetometerData', 'UIProgressView', 'GKInvite', 'UISearchBar', 'MKPlacemark', 'AVCaptureConnection', 'ALAssetsFilter', 'AVPlayerItemErrorLogEvent', 'NSJSONSerialization', 'AVAssetReaderVideoCompositionOutput', 'ABPersonViewController', 'CIDetector', 'GKTurnBasedMatchmakerViewController', 'MPMediaItemCollection', 'NSCondition', 'NSURLCredential', 'MIDINetworkConnection', 'NSDecimalNumberHandler', 'NSURLSessionConfiguration', 'EKCalendar', 'NSDictionary', 'CAPropertyAnimation', 'UIPercentDrivenInteractiveTransition', 'MKPolygon', 'AVAssetTrackSegment', 'NSExpressionDescription', 'UIViewController', 'NSURLAuthenticationChallenge', 'NSDirectoryEnumerator', 'MKDistanceFormatter', 'GCControllerElement', 'GKPeerPickerController', 'UITableViewController', 'GKNotificationBanner', 'MKPointAnnotation', 'NSCache', 'SKPhysicsJoint', 'NSXMLParser', 'MFMessageComposeViewController', 'AVCaptureSession', 'NSDataDetector', 'AVCaptureVideoPreviewLayer', 'NSURLComponents', 'UISnapBehavior', 'AVMetadataMachineReadableCodeObject', 'GLKTextureLoader', 'NSTextAttachment', 'NSException', 'UIMenuItem', 'CMMotionActivityManager', 'MKUserLocation', 'CIFeature', 'NSMachPort', 'ALAsset', 'NSURLSessionDownloadTask', 'MPMoviePlayerViewController', 'NSMutableOrderedSet', 'AVCaptureVideoDataOutput', 'NSCachedURLResponse', 'ALAssetsLibrary', 'NSInvocation', 'UILongPressGestureRecognizer', 'NSTextStorage', 'CIFaceFeature', 'MKMapSnapshot', 'GLKEffectPropertyFog', 'NSPersistentStoreRequest', 'AVAudioMixInputParameters', 'CAEmitterBehavior', 'PKPassLibrary', 'NSLock', 'UIDynamicBehavior', 'AVPlayerMediaSelectionCriteria', 'CALayer', 'UIBarButtonItem', 'AVAudioSessionRouteDescription', 'CLBeaconRegion', 'SKEffectNode', 'CABasicAnimation', 'AVVideoCompositionInstruction', 'AVMutableTimedMetadataGroup', 'EKRecurrenceEnd', 'NSTextContainer', 'TWTweetComposeViewController', 'UIScrollView', 'EKRecurrenceDayOfWeek', 'ASIdentifierManager', 'UIScreen', 'CLRegion', 'NSProcessInfo', 'GLKTextureInfo', 'AVCaptureMetadataOutput', 'NSTextTab', 'JSManagedValue', 'NSDate', 'UITextChecker', 'NSData', 'NSParagraphStyle', 'AVMutableMetadataItem', 'EKAlarm', 'NSMutableURLRequest', 'UIVideoEditorController', 'NSAtomicStore', 'UIResponder', 'AVCompositionTrackSegment', 'GCGamepadSnapshot', 'MPMediaEntity', 'GLKSkyboxEffect', 'UISwitch', 'EKStructuredLocation', 'UIGestureRecognizer', 'NSProxy', 'GLKBaseEffect', 'GKScoreChallenge', 'NSCoder', 'MPMediaPlaylist', 'NSDateComponents', 'EKEvent', 'NSDateFormatter', 'AVAssetWriterInputPixelBufferAdaptor', 'UICollectionViewFlowLayoutInvalidationContext', 'UITextField', 'CLPlacemark', 'AVCaptureOutput', 'NSPropertyDescription', 'GCGamepad', 'NSPersistentStoreCoordinator', 'GKMatchmaker', 'CIContext', 'NSThread', 'SKRequest', 'SKPhysicsJointSliding', 'NSPredicate', 'GKVoiceChat', 'SKCropNode', 'AVCaptureAudioPreviewOutput', 'NSStringDrawingContext', 'GKGameCenterViewController', 'UIPrintPaper', 'UICollectionViewLayoutInvalidationContext', 'GLKEffectPropertyTransform', 'UIDatePicker', 'MKDirections', 'ALAssetsGroup', 'CAEmitterCell', 'UIFont', 'MKPinAnnotationView', 'UIPickerView', 'UIImageView', 'SKNode', 'MPMediaQuerySection', 'GKFriendRequestComposeViewController', 'NSError', 'CTSubscriberInfo', 'AVPlayerItemAccessLog', 'MPMediaPropertyPredicate', 'CMLogItem', 'NSAutoreleasePool', 'NSSocketPort', 'AVAssetReaderTrackOutput', 'AVSpeechSynthesisVoice', 'UIImage', 'AVCaptureAudioChannel', 'GKTurnBasedExchangeReply', 'AVVideoCompositionLayerInstruction', 'AVSpeechSynthesizer', 'GKChallengeEventHandler', 'AVCaptureFileOutput', 'UIControl', 'SKPayment', 'ADInterstitialAd', 'AVAudioSessionDataSourceDescription', 'NSArray', 'GCControllerDirectionPad', 'NSFileManager', 'AVMutableAudioMixInputParameters', 'UIScreenEdgePanGestureRecognizer', 'CAKeyframeAnimation', 'EASession', 'UIInputView', 'NSHTTPCookieStorage', 'NSPointerFunctions', 'AVMediaSelectionOption', 'NSRunLoop', 'CAAnimationGroup', 'MKCircle', 'NSMigrationManager', 'UICollectionViewUpdateItem', 'NSMutableData', 'NSMutableParagraphStyle', 'GLKEffectProperty', 'SKShapeNode', 'MPMovieErrorLogEvent', 'MKPolygonView', 'UIAccelerometer', 'NSScanner', 'GKAchievementChallenge', 'AVAudioPlayer', 'AVVideoComposition', 'NKLibrary', 'NSPersistentStore', 'NSPropertyMapping', 'GKChallenge', 'NSURLProtectionSpace', 'ACAccountStore', 'UITextRange', 'NSComparisonPredicate', 'NSOutputStream', 'PKAddPassesViewController', 'CTTelephonyNetworkInfo', 'AVTextStyleRule', 'NSFetchedPropertyDescription', 'UIPageViewController', 'CATransformLayer', 'MCNearbyServiceAdvertiser', 'NSObject', 'MPMusicPlayerController', 'MKOverlayPathRenderer', 'GKAchievement', 'AVCaptureAudioFileOutput', 'TWRequest', 'SKLabelNode', 'MIDINetworkHost', 'MPMediaPredicate', 'AVFrameRateRange', 'NSIndexPath', 'AVVideoCompositionRenderContext', 'CADisplayLink', 'CAEAGLLayer', 'NSMutableString', 'NSMessagePort', 'AVAudioSessionChannelDescription', 'GLKView', 'UIActivityViewController', 'GKAchievementViewController', 'NSURLProtocol', 'NSCalendar', 'SKKeyframeSequence', 'AVMetadataItemFilter', 'NSMethodSignature', 'NSRegularExpression', 'EAGLSharegroup', 'AVPlayerItemVideoOutput', 'CIColor', 'UIDictationPhrase'])
COCOA_PROTOCOLS = set(['SKStoreProductViewControllerDelegate', 'AVVideoCompositionInstruction', 'AVAudioSessionDelegate', 'GKMatchDelegate', 'NSFileManagerDelegate', 'UILayoutSupport', 'NSCopying', 'UIPrintInteractionControllerDelegate', 'QLPreviewControllerDataSource', 'SKProductsRequestDelegate', 'NSTextStorageDelegate', 'MCBrowserViewControllerDelegate', 'UIViewControllerTransitionCoordinatorContext', 'NSTextAttachmentContainer', 'NSDecimalNumberBehaviors', 'NSMutableCopying', 'UIViewControllerTransitioningDelegate', 'UIAlertViewDelegate', 'AVAudioPlayerDelegate', 'MKReverseGeocoderDelegate', 'NSCoding', 'UITextInputTokenizer', 'GKFriendRequestComposeViewControllerDelegate', 'UIActivityItemSource', 'NSCacheDelegate', 'UITableViewDelegate', 'GKAchievementViewControllerDelegate', 'EKEventEditViewDelegate', 'NSURLConnectionDelegate', 'GKPeerPickerControllerDelegate', 'UIGuidedAccessRestrictionDelegate', 'AVSpeechSynthesizerDelegate', 'MFMailComposeViewControllerDelegate', 'AVPlayerItemLegibleOutputPushDelegate', 'ADInterstitialAdDelegate', 'AVAssetResourceLoaderDelegate', 'UITabBarControllerDelegate', 'SKPaymentTransactionObserver', 'AVCaptureAudioDataOutputSampleBufferDelegate', 'UIInputViewAudioFeedback', 'GKChallengeListener', 'UIPickerViewDelegate', 'UIWebViewDelegate', 'UIApplicationDelegate', 'GKInviteEventListener', 'MPMediaPlayback', 'MyClassJavaScriptMethods', 'AVAsynchronousKeyValueLoading', 'QLPreviewItem', 'NSPortDelegate', 'SKRequestDelegate', 'SKPhysicsContactDelegate', 'UIPageViewControllerDataSource', 'AVPlayerItemOutputPushDelegate', 'UICollectionViewDelegate', 'UIImagePickerControllerDelegate', 'UIToolbarDelegate', 'UIViewControllerTransitionCoordinator', 'NSURLConnectionDataDelegate', 'MKOverlay', 'CBCentralManagerDelegate', 'JSExport', 'NSTextLayoutOrientationProvider', 'UIPickerViewDataSource', 'UITextInputTraits', 'NSLayoutManagerDelegate', 'NSFetchedResultsControllerDelegate', 'ABPeoplePickerNavigationControllerDelegate', 'NSDiscardableContent', 'UITextFieldDelegate', 'GKGameCenterControllerDelegate', 'MPMediaPickerControllerDelegate', 'UIAppearance', 'UIPickerViewAccessibilityDelegate', 'UIScrollViewAccessibilityDelegate', 'ADBannerViewDelegate', 'NSURLSessionDelegate', 'NSXMLParserDelegate', 'UIViewControllerRestoration', 'UISearchBarDelegate', 'UIBarPositioning', 'CBPeripheralDelegate', 'UISearchDisplayDelegate', 'CAAction', 'PKAddPassesViewControllerDelegate', 'MCNearbyServiceAdvertiserDelegate', 'GKTurnBasedMatchmakerViewControllerDelegate', 'UIActionSheetDelegate', 'AVCaptureVideoDataOutputSampleBufferDelegate', 'UIAppearanceContainer', 'UIStateRestoring', 'NSURLSessionTaskDelegate', 'NSFilePresenter', 'UIViewControllerContextTransitioning', 'UITextInput', 'CBPeripheralManagerDelegate', 'UITextInputDelegate', 'NSFastEnumeration', 'NSURLAuthenticationChallengeSender', 'AVVideoCompositing', 'NSSecureCoding', 'MCAdvertiserAssistantDelegate', 'GKLocalPlayerListener', 'GLKNamedEffect', 'UIPopoverControllerDelegate', 'AVCaptureMetadataOutputObjectsDelegate', 'MFMessageComposeViewControllerDelegate', 'UITextSelecting', 'NSURLProtocolClient', 'UIVideoEditorControllerDelegate', 'UITableViewDataSource', 'UIDynamicAnimatorDelegate', 'NSURLSessionDataDelegate', 'UICollisionBehaviorDelegate', 'NSStreamDelegate', 'MCNearbyServiceBrowserDelegate', 'UINavigationControllerDelegate', 'MCSessionDelegate', 'UIViewControllerInteractiveTransitioning', 'GKTurnBasedEventListener', 'GLKViewDelegate', 'EAAccessoryDelegate', 'NSKeyedUnarchiverDelegate', 'NSMachPortDelegate', 'UIBarPositioningDelegate', 'ABPersonViewControllerDelegate', 'NSNetServiceBrowserDelegate', 'EKEventViewDelegate', 'UIScrollViewDelegate', 'NSURLConnectionDownloadDelegate', 'UIGestureRecognizerDelegate', 'UINavigationBarDelegate', 'GKVoiceChatClient', 'NSFetchedResultsSectionInfo', 'UIDocumentInteractionControllerDelegate', 'QLPreviewControllerDelegate', 'UIAccessibilityReadingContent', 'ABUnknownPersonViewControllerDelegate', 'GLKViewControllerDelegate', 'UICollectionViewDelegateFlowLayout', 'UISplitViewControllerDelegate', 'MKAnnotation', 'UIAccessibilityIdentification', 'ABNewPersonViewControllerDelegate', 'CAMediaTiming', 'AVCaptureFileOutputRecordingDelegate', 'UITextViewDelegate', 'UITabBarDelegate', 'GKLeaderboardViewControllerDelegate', 'MKMapViewDelegate', 'UIKeyInput', 'UICollectionViewDataSource', 'NSLocking', 'AVCaptureFileOutputDelegate', 'GKChallengeEventHandlerDelegate', 'UIObjectRestoration', 'CIFilterConstructor', 'AVPlayerItemOutputPullDelegate', 'EAGLDrawable', 'AVVideoCompositionValidationHandling', 'UIViewControllerAnimatedTransitioning', 'NSURLSessionDownloadDelegate', 'UIAccelerometerDelegate', 'UIPageViewControllerDelegate', 'UIDataSourceModelAssociation', 'AVAudioRecorderDelegate', 'GKSessionDelegate', 'NSKeyedArchiverDelegate', 'UIDynamicItem', 'CLLocationManagerDelegate', 'NSMetadataQueryDelegate', 'NSNetServiceDelegate', 'GKMatchmakerViewControllerDelegate', 'EKCalendarChooserDelegate'])
COCOA_PRIMITIVES = set(['ROTAHeader', '__CFBundle', 'MortSubtable', 'AudioFilePacketTableInfo', 'CGPDFOperatorTable', 'KerxStateEntry', 'ExtendedTempoEvent', 'CTParagraphStyleSetting', 'OpaqueMIDIPort', 'CFStreamErrorHTTP', '__CFMachPort', '_GLKMatrix4', 'ExtendedControlEvent', 'CAFAudioDescription', 'KernVersion0Header', 'CGTextDrawingMode', 'EKErrorCode', 'gss_buffer_desc_struct', 'AudioUnitParameterInfo', '__SCPreferences', '__CTFrame', '__CTLine', 'CFStreamSocketSecurityProtocol', 'gss_krb5_lucid_context_v1', 'OpaqueJSValue', 'TrakTableEntry', 'AudioFramePacketTranslation', 'CGImageSource', 'OpaqueJSPropertyNameAccumulator', 'JustPCGlyphRepeatAddAction', 'BslnFormat0Part', 'OpaqueMIDIThruConnection', 'opaqueCMBufferQueue', 'OpaqueMusicSequence', 'MortRearrangementSubtable', 'MixerDistanceParams', 'MorxSubtable', 'MIDIObjectPropertyChangeNotification', '__CFDictionary', 'CGImageMetadataErrors', 'CGPath', 'OpaqueMIDIEndpoint', 'ALMXHeader', 'AudioComponentPlugInInterface', 'gss_ctx_id_t_desc_struct', 'sfntFontFeatureSetting', 'OpaqueJSContextGroup', '__SCNetworkConnection', 'AudioUnitParameterValueTranslation', 'CGImageMetadataType', 'CGPattern', 'AudioFileTypeAndFormatID', 'CGContext', 'AUNodeInteraction', 'SFNTLookupTable', 'JustPCDecompositionAction', 'KerxControlPointHeader', 'PKErrorCode', 'AudioStreamPacketDescription', 'KernSubtableHeader', '__CFNull', 'AUMIDIOutputCallbackStruct', 'MIDIMetaEvent', 'AudioQueueChannelAssignment', '__CFString', 'AnchorPoint', 'JustTable', '__CFNetService', 'gss_krb5_lucid_key', 'CGPDFDictionary', 'MIDIThruConnectionParams', 'CAF_UUID_ChunkHeader', 'gss_krb5_cfx_keydata', '_GLKMatrix3', 'CGGradient', 'OpaqueMIDISetup', '_GLKMatrix2', 'JustPostcompTable', '__CTParagraphStyle', 'AudioUnitParameterHistoryInfo', 'OpaqueJSContext', 'CGShading', '__CFBinaryHeap', 'SFNTLookupSingle', '__CFHost', '__SecRandom', '__CTFontDescriptor', '_NSRange', 'sfntDirectory', 'AudioQueueLevelMeterState', 'CAFPositionPeak', '__CFBoolean', 'PropLookupSegment', '__CVOpenGLESTextureCache', 'sfntInstance', '_GLKQuaternion', 'KernStateEntry', '__SCNetworkProtocol', 'CAFFileHeader', 'KerxOrderedListHeader', 'CGBlendMode', 'STXEntryOne', 'CAFRegion', 'SFNTLookupTrimmedArrayHeader', 'KerxControlPointEntry', '__CFCharacterSet', 'OpaqueMusicTrack', '_GLKVector4', 'gss_OID_set_desc_struct', 'OpaqueMusicPlayer', '_CFHTTPAuthentication', 'CGAffineTransform', 'CAFMarkerChunk', 'AUHostIdentifier', 'ROTAGlyphEntry', 'BslnTable', 'gss_krb5_lucid_context_version', '_GLKMatrixStack', 'CGImage', 'AnkrTable', 'SFNTLookupSingleHeader', 'MortLigatureSubtable', 'AudioFile_SMPTE_Time', 'CAFUMIDChunk', 'SMPTETime', 'CAFDataChunk', 'CGPDFStream', 'AudioFileRegionList', 'STEntryTwo', 'SFNTLookupBinarySearchHeader', 'OpbdTable', '__CTGlyphInfo', 'BslnFormat2Part', 'KerxIndexArrayHeader', 'TrakTable', 'KerxKerningPair', '__CFBitVector', 'KernVersion0SubtableHeader', 'OpaqueAudioComponentInstance', 'AudioChannelLayout', '__CFUUID', 'MIDISysexSendRequest', '__CFNumberFormatter', 'CGImageSourceStatus', '__CFURL', 'AudioFileMarkerList', 'AUSamplerBankPresetData', 'CGDataProvider', 'AudioFormatInfo', '__SecIdentity', 'sfntCMapExtendedSubHeader', 'MIDIChannelMessage', 'KernOffsetTable', 'CGColorSpaceModel', 'MFMailComposeErrorCode', 'CGFunction', '__SecTrust', 'CFHostInfoType', 'KernSimpleArrayHeader', 'CGFontPostScriptFormat', 'KernStateHeader', 'AudioUnitCocoaViewInfo', 'CGDataConsumer', 'OpaqueMIDIDevice', 'OpaqueCMBlockBuffer', 'AnchorPointTable', 'CGImageDestination', 'CAFInstrumentChunk', 'AudioUnitMeterClipping', '__CFNumber', 'MorxChain', '__CTFontCollection', 'STEntryOne', 'STXEntryTwo', 'ExtendedNoteOnEvent', '__CFArray', 'CGColorRenderingIntent', 'KerxSimpleArrayHeader', 'MorxTable', '_GLKVector3', '_GLKVector2', 'MortTable', 'CGPDFBox', 'AudioUnitParameterValueFromString', '__CFSocket', 'ALCdevice_struct', 'MIDINoteMessage', 'sfntFeatureHeader', 'CGRect', '__SCNetworkInterface', '__CFTree', 'MusicEventUserData', 'TrakTableData', 'MortContextualSubtable', '__CTRun', 'AudioUnitFrequencyResponseBin', 'MortChain', 'MorxInsertionSubtable', 'CGImageMetadata', 'gss_auth_identity', 'AudioUnitMIDIControlMapping', 'CAFChunkHeader', 'PropTable', 'CGPDFScanner', 'OpaqueMusicEventIterator', '__CFFileSecurity', 'AudioUnitNodeConnection', 'OpaqueMIDIDeviceList', 'ExtendedAudioFormatInfo', 'CGRectEdge', 'sfntFontDescriptor', '__CFRunLoopObserver', 'CGPatternTiling', 'MIDINotification', 'MorxLigatureSubtable', 'SFNTLookupSegment', 'MessageComposeResult', 'MIDIThruConnectionEndpoint', 'MusicDeviceStdNoteParams', 'opaqueCMSimpleQueue', 'ALCcontext_struct', 'OpaqueAudioQueue', 'PropLookupSingle', 'CGColor', 'AudioOutputUnitStartAtTimeParams', 'gss_name_t_desc_struct', 'CGFunctionCallbacks', 'CAFPacketTableHeader', 'AudioChannelDescription', 'sfntFeatureName', 'MorxContextualSubtable', 'CVSMPTETime', 'AudioValueRange', 'CGTextEncoding', 'AudioStreamBasicDescription', 'AUNodeRenderCallback', 'AudioPanningInfo', '__CFData', '__CFDate', 'KerxOrderedListEntry', '__CFAllocator', 'OpaqueJSPropertyNameArray', '__SCDynamicStore', 'OpaqueMIDIEntity', 'CFHostClientContext', 'CFNetServiceClientContext', 'AudioUnitPresetMAS_SettingData', 'opaqueCMBufferQueueTriggerToken', 'AudioUnitProperty', 'CAFRegionChunk', 'CGPDFString', '__CFWriteStream', '__CFAttributedString', '__CFStringTokenizer', 'JustWidthDeltaEntry', '__CFSet', 'sfntVariationAxis', '__CFNetDiagnostic', 'CAFOverviewSample', 'sfntCMapEncoding', 'CGVector', '__SCNetworkService', 'opaqueCMSampleBuffer', 'AUHostVersionIdentifier', 'AudioBalanceFade', 'sfntFontRunFeature', 'KerxCoordinateAction', 'sfntCMapSubHeader', 'CVPlanarPixelBufferInfo', 'AUNumVersion', '__CFTimeZone', 'AUSamplerInstrumentData', 'AUPreset', '__CTRunDelegate', 'OpaqueAudioQueueProcessingTap', 'KerxTableHeader', '_NSZone', 'OpaqueExtAudioFile', '__CFRunLoopSource', 'KerxAnchorPointAction', 'OpaqueJSString', 'AudioQueueParameterEvent', '__CFHTTPMessage', 'OpaqueCMClock', 'ScheduledAudioFileRegion', 'STEntryZero', 'gss_channel_bindings_struct', 'sfntVariationHeader', 'AUChannelInfo', 'UIOffset', 'GLKEffectPropertyPrv', 'KerxStateHeader', 'CGLineJoin', 'CGPDFDocument', '__CFBag', 'CFStreamErrorHTTPAuthentication', 'KernOrderedListHeader', '__SCNetworkSet', '__SecKey', 'MIDIObjectAddRemoveNotification', 'sfntDescriptorHeader', 'AudioUnitParameter', 'JustPCActionSubrecord', 'AudioComponentDescription', 'AudioUnitParameterValueName', 'AudioUnitParameterEvent', 'KerxControlPointAction', 'AudioTimeStamp', 'KernKerningPair', 'gss_buffer_set_desc_struct', 'MortFeatureEntry', 'FontVariation', 'CAFStringID', 'LcarCaretClassEntry', 'AudioUnitParameterStringFromValue', 'ACErrorCode', 'ALMXGlyphEntry', 'LtagTable', '__CTTypesetter', 'AuthorizationOpaqueRef', 'UIEdgeInsets', 'CGPathElement', 'CAFMarker', 'KernTableHeader', 'NoteParamsControlValue', 'SSLContext', 'gss_cred_id_t_desc_struct', 'AudioUnitParameterNameInfo', '__SecCertificate', 'CGDataConsumerCallbacks', 'CGInterpolationQuality', 'CGLineCap', 'MIDIControlTransform', 'BslnFormat1Part', 'CGPDFArray', '__SecPolicy', 'AudioConverterPrimeInfo', '__CTTextTab', '__CFNetServiceMonitor', 'AUInputSamplesInOutputCallbackStruct', '__CTFramesetter', 'CGPDFDataFormat', 'STHeader', 'CVPlanarPixelBufferInfo_YCbCrPlanar', 'MIDIValueMap', 'JustDirectionTable', '__SCBondStatus', 'SFNTLookupSegmentHeader', 'OpaqueCMMemoryPool', 'CGPathDrawingMode', 'CGFont', '__SCNetworkReachability', 'AudioClassDescription', 'CGPoint', 'CAFStrings', '__CFNetServiceBrowser', 'opaqueMTAudioProcessingTap', 'sfntNameRecord', 'CGPDFPage', 'CGLayer', 'ComponentInstanceRecord', 'CAFInfoStrings', 'HostCallbackInfo', 'MusicDeviceNoteParams', 'KernIndexArrayHeader', 'CVPlanarPixelBufferInfo_YCbCrBiPlanar', 'MusicTrackLoopInfo', 'opaqueCMFormatDescription', 'STClassTable', 'sfntDirectoryEntry', 'OpaqueCMTimebase', 'CGDataProviderDirectCallbacks', 'MIDIPacketList', 'CAFOverviewChunk', 'MIDIPacket', 'ScheduledAudioSlice', 'CGDataProviderSequentialCallbacks', 'AudioBuffer', 'MorxRearrangementSubtable', 'CGPatternCallbacks', 'AUDistanceAttenuationData', 'MIDIIOErrorNotification', 'CGPDFContentStream', 'IUnknownVTbl', 'MIDITransform', 'MortInsertionSubtable', 'CABarBeatTime', 'AudioBufferList', 'KerxSubtableHeader', '__CVBuffer', 'AURenderCallbackStruct', 'STXEntryZero', 'JustPCDuctilityAction', 'OpaqueAudioQueueTimeline', 'OpaqueMIDIClient', '__CFPlugInInstance', 'AudioQueueBuffer', '__CFFileDescriptor', 'AudioUnitConnection', '_GKTurnBasedExchangeStatus', 'LcarCaretTable', 'CVPlanarComponentInfo', 'JustWidthDeltaGroup', 'OpaqueAudioComponent', 'ParameterEvent', '__CVPixelBufferPool', '__CTFont', 'OpaqueJSClass', 'CGColorSpace', 'CGSize', 'AUDependentParameter', 'MIDIDriverInterface', 'gss_krb5_rfc1964_keydata', '__CFDateFormatter', 'LtagStringRange', 'CFNetServiceMonitorType', 'gss_iov_buffer_desc_struct', 'AUPresetEvent', 'CFNetServicesError', 'KernOrderedListEntry', '__CFLocale', 'gss_OID_desc_struct', 'AudioUnitPresetMAS_Settings', 'AudioFileMarker', 'JustPCConditionalAddAction', 'BslnFormat3Part', '__CFNotificationCenter', 'MortSwashSubtable', 'AUParameterMIDIMapping', 'OpaqueAudioConverter', 'MIDIRawData', 'CFNetDiagnosticStatusValues', 'sfntNameHeader', '__CFRunLoop', 'MFMailComposeResult', 'CATransform3D', 'OpbdSideValues', 'CAF_SMPTE_Time', 'JustPCAction', 'CGPathElementType', '__CFRunLoopTimer', '__CFError', 'AudioFormatListItem', '__CFReadStream', 'AudioUnitExternalBuffer', 'AudioFileRegion', 'AudioValueTranslation', 'CGImageMetadataTag', 'CAFPeakChunk', 'AudioBytePacketTranslation', 'CFNetworkErrors', 'sfntCMapHeader', '__CFURLEnumerator', '__CFCalendar', '__CFMessagePort', 'STXHeader', 'CGPDFObjectType', 'SFNTLookupArrayHeader'])


if __name__ == '__main__':
    import os
    import re

    FRAMEWORKS_PATH = '/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS7.0.sdk/System/Library/Frameworks/'
    frameworks = os.listdir(FRAMEWORKS_PATH)

    all_interfaces = set()
    all_protocols  = set()
    all_primitives = set()
    for framework in frameworks:
        frameworkHeadersDir = FRAMEWORKS_PATH + framework + '/Headers/'
        if not os.path.exists(frameworkHeadersDir):
            continue

        headerFilenames = os.listdir(frameworkHeadersDir)

        for f in headerFilenames:
            if not f.endswith('.h'):
                continue

            headerFilePath = frameworkHeadersDir + f
            content = open(headerFilePath).read()
            res = re.findall('(?<=@interface )\w+', content)
            for r in res:
                all_interfaces.add(r)

            res = re.findall('(?<=@protocol )\w+', content)
            for r in res:
                all_protocols.add(r)

            res = re.findall('(?<=typedef enum )\w+', content)
            for r in res:
                all_primitives.add(r)

            res = re.findall('(?<=typedef struct )\w+', content)
            for r in res:
                all_primitives.add(r)

            res = re.findall('(?<=typedef const struct )\w+', content)
            for r in res:
                all_primitives.add(r)


    print("ALL interfaces: \n")
    print(all_interfaces)

    print("\nALL protocols: \n")
    print(all_protocols)

    print("\nALL primitives: \n")
    print(all_primitives)
